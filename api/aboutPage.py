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
import aboutView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class about(baseObject.baseHTTPObject):
	'''
	Manages the about page.
	'''
	def get(self):
		'''
		GET verb call
		
		returns the about page template.
		
		Args:
			None
			
		Returns:
			HTML template; see aboutView.py and templates for more info.
			
		'''
		view = aboutView.aboutView()
		
		return view.returnData()


app = web.application(baseObject.urls, globals())
