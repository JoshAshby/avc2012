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
import scoreboardView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class all(baseObject.baseHTTPObject):
	'''
	Manages the heavy lifting of whos the top 5 and who won what.
	'''
	def get(self):
		'''
		GET verb call
		
		returns a html template with a list of the various standings
		
		Args:
			None
			
		Returns:
		HTML template. See standView.py and templates.py for more info.	
			
		'''
		pass # still have to write this logic I guess.

app = web.application(baseObject.urls, globals())
