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
	Public interface to see a list of teams and general info.
	'''
	def get(self):
		'''
		GET verb call
		
		returns a template filled with info about each team in a table.
		
		Args:
			None
			
		Returns:
			HTML template; see listView.py and templates for more info.
			
		'''
		bots = database.view("bots/Bots").all()
		botNew = []
		
		for i in bots:
			botNew.append(i['value'])


		view = listView.listView(data=botNew)
		
		return view.returnData()


app = web.application(baseObject.urls, globals())
