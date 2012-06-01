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


class adminMainView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminMainView'])
		page.title = (titleHalf + 'Admin')
		page.vehicleType = ''
		
		web.header('Content-Type', "text/html")
		
		return page


class adminScoreboardView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminScoreboardView'])
		page.title = (titleHalf + 'Admin Scoreboard')
		page.vehicleType = ''
		
		web.header('Content-Type', "text/html")
		
		return page


class adminTeamListView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminTeamListView'])
		page.title = (titleHalf + 'Admin Teams')
		page.content = ''
		page.vehicleType = ''

		for bot in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminView'])
			partial.teamId = bot['id']
			partial.teamName = bot['team']
			partial.botName = bot['name']
			partial.location = bot['location']
			partial.builders = bot['builders']
			partial.checkin = bot['checkedIn']
			page.content += str(partial)
		
		web.header('Content-Type', "text/html")
		
		return page


class adminTeamView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminTeamView'])
		page.title = (titleHalf + 'Admin Team Info')
		page.vehicleType = ''
		page.content = ''
		page.id = self.data['bot']['id']
		page.team = self.data['bot']['team']
		page.name = self.data['bot']['name']
		page.location = self.data['bot']['location']
		page.builders = self.data['bot']['builders']
		page.checkin = self.data['bot']['checkedIn']
		page.vehicleType = self.data['bot']['vehicleType']
		heatList = []
		for heat in self.data['heat']:
			heatList.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')
		page.heat1 = heatList
		page.heat2 = heatList
		page.heat3 = heatList
			
		web.header('Content-Type', "text/html")
		
		return page

class adminScheduleView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminScheduleView'])
		page.title = (titleHalf + 'Admin Team Info')
		page.content = ''
		page.vehicleType = ''

		print self.data

		for heat in self.data:
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatView'])
			partial.bots = ''
			partial.heat = heat

			for bot in heat:
				indivBotPartial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminView'])
				indivBotPartial.teamId = bot['id']
				indivBotPartial.teamName = bot['team']
				indivBotPartial.botName = bot['name']
				indivBotPartial.location = bot['location']
				indivBotPartial.builders = bot['builders']
				indivBotPartial.checkin = bot['checkedIn']

				partial.bots += str(indivBotPartial)

			page.content += str(partial)


		web.header('Content-Type', "text/html")
		
		return page
