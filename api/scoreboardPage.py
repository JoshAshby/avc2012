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
from botsDocument import *
from heatDocument import *
from adminDocument import *
import scoreboardView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class index(baseObject.baseHTTPObject):
	'''
	Manages the scoreboard view
	'''
	def get(self):
		'''
		GET verb call
		
		returns the main scoreboard template
		
		Args:
			None
			
		Returns:
			HTML template, see scoreboardView.py and templates.py for more info.
			
		'''
		view = scoreboardView.scoreboardView()
		
		return view.returnData()


@baseObject.route('/checkIn/')
class checkIn(baseObject.baseHTTPObject):
	'''
	Manages the check in table in the scoreboard.
	'''
	def get(self):
		'''
		GET verb call
		
		Returns a partial template of robots who have checked in.

		Args:
			None	

		Returns:
			table row formated data to be pulled right into a table body.
			
		'''
		bots = database.view("bots/Bots").all()
		botNew = []
		
		for i in bots:
			if i['value']['checkedIn'] is 1:
				botNew.append(i['value'])


		view = scoreboardView.tableView(data=botNew)
		
		return view.returnData()


@baseObject.route('/heat/(.*)/')
class heat(baseObject.baseHTTPObject):
	'''
	Manages views of heats.

	**TODO**: Update this for the new storage of heats in botsDocs not heatDocs
	'''
	def get(self):
		'''
		GET verb call

		Returns a partial template of robots in a heat.

		Args:
			heat - int of the heat number
			
		Returns:
			table row formated data to be pulled right into a table body.
			
		'''
		
		heat = self.hasMember('heat', True)
		
		bots = database.view("bots/Bots").all()

		spots = []

		for bot in bots:
			bot = bot['value']
			if bot['checkedIn']:
				if bot['heatOneWave'] == heat:
					spots.append(bot)
				if bot['heatTwoWave'] == heat:
					spots.append(bot)
				if bot['heatThreeWave'] == heat:
					spots.append(bot)

		view = scoreboardView.heatView(data=spots)
		
		return view.returnData()


@baseObject.route('/admin/')
class admin(baseObject.baseHTTPObject):
	'''
	Just a call to figure out what view to be on
	'''
	def get(self):
		'''
		GET verb call

		returns JSON of which view to be on.
		
		Args:
			None
			
		Returns:
			JSON object silimar to: {"admin": {"viewScreen": "2/1"}} 
			
		'''
		admin = database.view("admin/Admin", key=0).first()['value']

		view = scoreboardView.adminView(data=admin)
		
		return view.returnData()



app = web.application(baseObject.urls, globals())
