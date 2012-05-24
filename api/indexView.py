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
import baseView
import templates


class indexView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'index': self.data})
		
	def HTML(self):
		page = templates.indexTemplate(file=templates.templateSet['index'])
		page.title = (titleHalf + 'Landing')
		page.content = self.data
		
		web.header('Content-Type', "text/html")
		
		return page
