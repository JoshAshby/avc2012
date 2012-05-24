#!/usr/bin/env python
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
import baseObject

baseObject.urlReset()


@baseObject.route('/(.*)/')
class test(baseObject.baseHTTPObject):
	def get(self):	
		'''
		GET verb call
		
		Returns:
		'''
		bar = self.hasMember('barcode')
		
		pass


app = web.application(baseObject.urls, globals())
