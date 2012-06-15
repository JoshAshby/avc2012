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


class scoreboardView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is a web browser application and does not return JSON, Sorry!'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['scoreboardView'])
		page.title = (titleHalf + 'Scoreboard')
		page.checkIn = ''
		page.schedule = ''

		web.header('Content-Type', 'text/html')

		return page


class listView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'bots': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['listViewBody'])
		page.content = ''
		for bot in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listViewBody'])
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			partial.checkin = bot['checkedIn']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page


class standView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'bots': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['standViewBody'])
		page.content = ''

		for bot in self.data:
			bot = self.data[bot]
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listStandViewBody'])
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			partial.time = bot['time']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page


class heatView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'bots': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['listViewBody'])
		page.content = ''
		for bot in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listViewBody'])
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page


class tableView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'bots': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['listViewBody'])
		page.content = ''
		for bot in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listViewBody'])
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.location = bot['location']
			partial.botName = bot['name']
			partial.builders = bot['builders']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page


class adminView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'admin': self.data})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminMainView'])
		page.title = (titleHalf + 'Admin')

		web.header('Content-Type', 'text/html')

		return page
