#!/usr/bin/env python2
"""
Official 2012 SparkFun Electronics AVC Scoreboard App

For more information, see: https://github.com/JoshAshby/avc2012

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import web
import json
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from configSub import *
import adminView
import baseObject
from adminDocument import *
from botsDocument import *
from heatDocument import *

baseObject.urlReset()


@baseObject.route('/')
class adminMain(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		view = adminView.adminMainView()
		
		return view.returnData()


@baseObject.route('/scoreboard/')
class adminScoreboard(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		view = adminView.adminScoreboardView()
		
		return view.returnData()

	def post(self):
		'''
		POST verb call

		Args:

		Returns:

		'''
		nextView = str(self.hasMember('view'))

		docId = database.view("admin/Admin", key=0).first()['value']['_id']

		doc = adminDoc.get(docId)

		doc.viewScreen = nextView
		doc.save()
		

@baseObject.route('/teams/')
class adminTeamList(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		bots = database.view("bots/Bots").all()
		botNew = []
		
		for i in bots:
			botNew.append(i['value'])

		view = adminView.adminTeamListView(data=botNew)
		
		return view.returnData()

	def post(self):
		'''
		POST verb call
		
		Marks the given botId number as checked in
		
		Args:

		Returns:

		'''
		botId = str(self.hasMember('botId'))

		docId = database.view("bots/Bots", key=0).first()['value']['_id']

		doc = botsDoc.get(docId)

		doc.checkedIn = 1

		doc.save()


@baseObject.route('/teams/(.*)/')
class adminTeam(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		bot = int(self.hasMember('botId'))

		doc = database.view("bots/Bots", key=bot).first()['value']
		
		botInfo = doc
		view = adminView.adminTeamView(data=botInfo)
		
		return view.returnData()

	def post(self):
		'''
		POST verb call
		
		Updates the given information in the database

		Args:

		Returns:

		'''
		botId = str(self.hasMember('botId'))

		docId = database.view("bots/Bots", key=botId).first()['value']['_id']

		doc = botDocument.get(docId)
		
		name = str(self.hasMember('name', True))
		builders = str(self.hasMember('builders', True))
		checkedIn = int(self.hasMember('checkedIn', True))
		team = str(self.hasMember('team', True))
		vehicleType = int(self.hasMember('vehicleType', True))
		location = str(self.hasMember('location', True))

		if name: doc.name = name
		if builders: doc.builders = builders
		if checkedIn: doc.checkedIn = checkedIn
		if team: doc.team = team
		if vehicleType: doc.vehicleType = vehicleType
		
		doc.save()
		

@baseObject.route('/time/(.*)/')
class adminTime(baseObject.baseHTTPObject):
	'''

	'''
	def post(self):
		'''
		POST verb call
		
		Updates heat times for the given botId

		Args:

		Returns:

		'''
		botId = int(self.hasMember('botId'))

		docId = database.view("bots/Bots", key=botId).first()['value']['_id']

		doc = botDocument.get(docId)
		
		heatId = int(self.hasMember('heatId', True))

		
		
		doc.save()


@baseObject.route('/schedule/')
class adminSchedule(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		view = adminView.adminScheduleView()
		
		return view.returnData()

	def post(self):
		'''
		POST verb call

		Args:

		Returns:

		'''
		heatId = int(self.hasMember('heatId'))
		


		doc = botDocument.get(docId)

		doc.save()


app = web.application(baseObject.urls, globals())
