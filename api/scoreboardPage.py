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
import scoreboardView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class index(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		view = scoreboardView.scoreboardView()
		
		return view.returnData()

@baseObject.route('/checkIn/')
class checkIn(baseObject.baseHTTPObject):
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
			if i['value']['checkedIn'] is 1:
				botNew.append(i['value'])


		view = scoreboardView.tableView(data=botNew)
		
		return view.returnData()


@baseObject.route('/heat/(.*)/')
class heatLineUp(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		heat = int(self.hasMember('heat'))

		bots = database.view("bots/Bots").all()

		lineUp = heatDoc.view("schedule/Schedule", key=heat).first()

		spots = []

		for bot in lineUp['bots']:
			spots.append(bots[int(bot)]['value'])

		view = scoreboardView.heatView(data=spots)
		
		return view.returnData()


app = web.application(baseObject.urls, globals())
