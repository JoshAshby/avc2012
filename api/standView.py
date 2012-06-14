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
		return json.dumps({'topThree': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['standView'])
		page.title = (titleHalf + 'Top 3')
		page.contentair = ''
		page.contentground = ''

		for bot in self.data['air']:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listStandView'])
			partial.place = bot
			bot = self.data['air'][bot]
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			partial.time = bot['time']

			page.contentair += str(partial)
		
		for bot in self.data['ground']:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listStandView'])
			partial.place = bot
			bot = self.data['air'][bot]
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			partial.time = bot['time']

			page.contentground += str(partial)

		web.header('Content-Type', "text/html")
		
		return page
