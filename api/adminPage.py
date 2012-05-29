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
		print docId

		doc = adminDoc.get(docId)

		doc.viewScreen = nextView
		doc.save()
		

@baseObject.route('/teams/')
class adminTeam(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		view = adminView.adminTeamView()
		
		return view.returnData()

app = web.application(baseObject.urls, globals())
