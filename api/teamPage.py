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
from picture import *
import listView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class all(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		bots = database.view("bots/Bots").all()
		
		for i in bots:
			i = i['value']

		view = listView.listView(data=bots)
		
		return view.returnData()


@baseObject.route('/(.*)')
class all(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		botId = int(self.hasMember('id'))

		teamInfo = botDoc.view("bots/Bots" key=botId).first()
		
		view = teamView.teamView(data=bots)
		
		return view.returnData()



app = web.application(baseObject.urls, globals())
