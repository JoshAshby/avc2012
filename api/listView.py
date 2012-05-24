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


class listView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'bots': self.data})
		
	def HTML(self):
		page = templates.listViewTemplate(file=templates.mainTemplateSet['listView'])
		page.title = (titleHalf + 'List-O-Bots')
		page.content = ''
		for bot in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listView'])
			bot = bot['value']
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			partial.checkin = bot['checkedIn']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page
