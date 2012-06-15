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

		for wave in self.data['waves']:
			page.waves += ("<option value=" + wave['num'] + "." + wave['id'] + ">" + wave['num'] + "</option>")

		page.current = self.data['current']
		page.upnext = self.data['upnext']
		
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
		if self.data['bot']['vehicleType'] is 0:
			page = templates.genericTemplate(file=templates.mainTemplateSet['adminTeamView'])
		else:
			page = templates.genericTemplate(file=templates.mainTemplateSet['adminTeamAirView'])
			page.heat1takeoff = 0
			page.heat2takeoff = 0
			page.heat3takeoff = 0
			page.heat1boxland = 0
			page.heat2boxland = 0
			page.heat3boxland = 0
			page.heat1parkinglot = 0
			page.heat2parkinglot = 0
			page.heat3parkinglot = 0
			page.heat1none = 0
			page.heat2none = 0
			page.heat3none = 0

			if self.data['bot']['heatOneBonus'] is 0:
				page.heat1none = 1
			elif self.data['bot']['heatOneBonus'] is 2:
				page.heat1takeoff = 1
				page.heat1none = 1
			elif self.data['bot']['heatOneBonus'] is 3:
				page.heat1boxland = 1
			elif self.data['bot']['heatOneBonus'] is 4:
				page.heat1parkinglot = 1
			elif self.data['bot']['heatOneBonus'] is 23:
				page.heat1takeoff = 1
				page.heat1boxland = 1
			elif self.data['bot']['heatOneBonus'] is 24:
				page.heat1takeoff = 1
				page.heat1parkinglot = 1
			
			if self.data['bot']['heatTwoBonus'] is 0:
				page.heat2none = 1
			elif self.data['bot']['heatTwoBonus'] is 2:
				page.heat2takeoff = 1
				page.heat2none = 1
			elif self.data['bot']['heatTwoBonus'] is 3:
				page.heat2boxland = 1
			elif self.data['bot']['heatTwoBonus'] is 4:
				page.heat2parkinglot = 1
			elif self.data['bot']['heatTwoBonus'] is 23:
				page.heat2takeoff = 1
				page.heat2boxland = 1
			elif self.data['bot']['heatTwoBonus'] is 24:
				page.heat2takeoff = 1
				page.heat2parkinglot = 1

			if self.data['bot']['heatThreeBonus'] is 0:
				page.heat3none = 1
			elif self.data['bot']['heatThreeBonus'] is 2:
				page.heat3takeoff = 1
				page.heat3none = 1
			elif self.data['bot']['heatThreeBonus'] is 3:
				page.heat3boxland = 1
			elif self.data['bot']['heatThreeBonus'] is 4:
				page.heat3parkinglot = 1
			elif self.data['bot']['heatThreeBonus'] is 23:
				page.heat3takeoff = 1
				page.heat3boxland = 1
			elif self.data['bot']['heatThreeBonus'] is 24:
				page.heat3takeoff = 1
				page.heat3parkinglot = 1

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
		
		for heat in self.data['heats']:
			for wave in self.data['heats'][heat]:
				partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBotView'])

				partial.content = ''

				for i in self.data['waves']:
					if wave is i['value']['_id']:
						waves = i['value']
				
				partial.wave = waves['wave']
				partial.heat = waves['heat']
				partial.time = waves['time']
				partial._id = waves['_id']

				if waves['vehicleType'] is 0:
					vehicle = "Ground"
				else:
					vehicle = "Air"
				partial.vehicle = vehicle


				for bot in self.data['heats'][heat][wave]:
					partialBot = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminView'])
					partialBot.botName = bot['name']
					partialBot.teamName = bot['team']
					partialBot.checkin = bot['checkedIn']
					partialBot.teamId = bot['id']
					partialBot.location = bot['location']
					partialBot.builders = bot['builders']
				
					if bot['vehicleType'] is 0:
						vehicle = "Ground"
					else:
						vehicle = "Air"
					partialBot.vehicle = vehicle
					partialBot.vechileType = bot['vehicleType']
					partial.content += str(partialBot)
				
				page.content += str(partial)


		web.header('Content-Type', "text/html")
		
		return page


class adminHeatBotBodyView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatBotBodyView'])
		page.title = (titleHalf + 'Admin Heat Bots')
		page.content = ''
		page.vehicleType = ''
		
		for heat in self.data['heats']:
			for wave in self.data['heats'][heat]:
				partial = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBotBodyView'])

				partial.content = ''

				for i in self.data['waves']:
					if wave is i['value']['_id']:
						waves = i['value']
				
				partial.wave = waves['wave']
				partial.heat = waves['heat']
				partial.time = waves['time']
				partial._id = waves['_id']

				if waves['vehicleType'] is 0:
					vehicle = "Ground"
				else:
					vehicle = "Air"
				partial.vehicle = vehicle


				for bot in self.data['heats'][heat][wave]:
					partialBot = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBodyView'])
					partialBot.botName = bot['name']
					partialBot.teamName = bot['team']
					partialBot.checkin = bot['checkedIn']
					partialBot.teamId = bot['id']
					partialBot.location = bot['location']
					partialBot.builders = bot['builders']
				
					if bot['vehicleType'] is 0:
						vehicle = "Ground"
					else:
						vehicle = "Air"
					partialBot.vehicle = vehicle
					partialBot.vechileType = bot['vehicleType']
					partial.content += str(partialBot)
				
				page.content += str(partial)


		web.header('Content-Type', "text/html")
		
		return page


class adminHeatPitView(baseView.baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'error': 'This is an HTML only page, no JSON please.'})
		
	def HTML(self):
		page = templates.genericTemplate(file=templates.mainTemplateSet['adminHeatPitView'])
		page.title = (titleHalf + 'Admin Heat Pit')
		page.content = ''
		page.vehicleType = ''
		page.current = ''
		page.upnext = ''
		
		for bot in self.data['current']:
			partialBot = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBodyView'])
			partialBot.botName = bot['name']
			partialBot.teamName = bot['team']
			partialBot.checkin = bot['checkedIn']
			partialBot.teamId = bot['id']
			partialBot.location = bot['location']
			partialBot.builders = bot['builders']
		
			if bot['vehicleType'] is 0:
				vehicle = "Ground"
			else:
				vehicle = "Air"
			partialBot.vehicle = vehicle
			partialBot.vechileType = bot['vehicleType']
			page.current += str(partialBot)

		for bot in self.data['upnext']:
			partialBot = templates.PartialListRow(file=templates.partialTemplateSet['row_listAdminHeatBodyView'])
			partialBot.botName = bot['name']
			partialBot.teamName = bot['team']
			partialBot.checkin = bot['checkedIn']
			partialBot.teamId = bot['id']
			partialBot.location = bot['location']
			partialBot.builders = bot['builders']
		
			if bot['vehicleType'] is 0:
				vehicle = "Ground"
			else:
				vehicle = "Air"
			partialBot.vehicle = vehicle
			partialBot.vechileType = bot['vehicleType']
			page.upnext += str(partialBot)
		
		
		web.header('Content-Type', "text/html")
		
		return page
