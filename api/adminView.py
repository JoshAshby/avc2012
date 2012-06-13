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
		page.waves = ''

		print self.data

		for wave in self.data['waves']:
			page.waves += ("<option value=" + wave['num'] + "." + wave['id'] + ">" + wave['num'] + "</option>")

		page.current = self.data['current']
		
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
		
		heat1List = []
		for heat in self.data['heat1']:
			heat1List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		heat2List = []
		for heat in self.data['heat2']:
			heat2List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		heat3List = []
		for heat in self.data['heat3']:
			heat3List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		page.heat1 = heat1List
		page.heat2 = heat2List
		page.heat3 = heat3List

		page.heat1time = self.data['bot']['heatOneTime']
		page.heat2time = self.data['bot']['heatTwoTime']
		page.heat3time = self.data['bot']['heatThreeTime']

		page.heat1bonus = self.data['bot']['heatOneBonus'] 
		page.heat2bonus = self.data['bot']['heatTwoBonus']
		page.heat3bonus = self.data['bot']['heatThreeBonus']

		page.heat1id = self.data['bot']['heatOneWave']
		page.heat2id = self.data['bot']['heatTwoWave']
		page.heat3id = self.data['bot']['heatThreeWave']

		web.header('Content-Type', "text/html")
		
		return page


class adminTeamNewView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminTeamNewView'])
		page.title = (titleHalf + 'Admin New Team')
		page.vehicleType = ''
		page.content = ''

		heat1List = []
		for heat in self.data['heat1']:
			heat1List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		heat2List = []
		for heat in self.data['heat2']:
			heat2List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		heat3List = []
		for heat in self.data['heat3']:
			heat3List.append('<option value="' + str(heat['id']) + '">' + str(heat['num']) + '</option>')

		page.heat1 = heat1List
		page.heat2 = heat2List
		page.heat3 = heat3List
			
		web.header('Content-Type', "text/html")
		
		return page


class adminHeatView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatListView'])
		page.title = (titleHalf + 'Admin Heat Schedule')
		page.content = ''
		page.vehicleType = ''

		for heat in self.data:
			heat = heat['value']

			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatView'])

			partial.heat = heat['heat']
			partial.wave = heat['wave']
			partial.time = heat['time']
			partial._id = heat["_id"]
			partial.vehicleType = heat['vehicleType']
			if heat['vehicleType'] is 0:
				vehicleType = "Ground"
			else:
				vehicleType = "Air"

			partial.vehicle = vehicleType

			page.content += str(partial)

		web.header('Content-Type', "text/html")
		
		return page


class adminHeatEditView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatEditView'])
		page.title = (titleHalf + 'Admin Heat Edit')
		page.content = ''
		page.vehicleType = ''

		page._id = self.data['_id']
		page.heat = self.data['heat']
		page.wave = self.data['wave']
		page.time = self.data['time']
		page.vehicleType = self.data['vehicleType']

		web.header('Content-Type', "text/html")
		
		return page


class adminHeatNewView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatNewView'])
		page.title = (titleHalf + 'Admin New Heat')
		page.content = ''
		page.vehicleType = ''

		web.header('Content-Type', "text/html")
		
		return page


class adminHeatBotView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatBotView'])
		page.title = (titleHalf + 'Admin Heat Bots')
		page.content = ''
		page.vehicleType = ''

		'''for wave in dict(self.data['heatOne']):
			partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBotView'])
			print wave

			for bot in heat:
				partialBot = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminView'])
				partialBot.botName = bot['name']
				partialBot.teamName = bot['team']

				if bot['vehicleType'] is 0:
					vehicleType = "Ground"
				else:
					vehicleType = "Air"
				partialBot.vehicle = vehicle
				partialBot.vechileType = bot['vehicleType']

			page.content += str(partial)'''


		web.header('Content-Type', "text/html")
		
		return page
