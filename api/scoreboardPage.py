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
from heatDocument import *
from adminDocument import *
import scoreboardView
import baseObject
import datetime
import operator

baseObject.urlReset()


@baseObject.route('/')
class index(baseObject.baseHTTPObject):
	'''
	Manages the scoreboard view
	'''
	def get(self):
		'''
		GET verb call
		
		returns the main scoreboard template
		
		Args:
			None
			
		Returns:
			HTML template, see scoreboardView.py and templates.py for more info.
			
		'''
		view = scoreboardView.scoreboardView()
		
		return view.returnData()


@baseObject.route('/checkIn/')
class checkIn(baseObject.baseHTTPObject):
	'''
	Manages the check in table in the scoreboard.
	'''
	def get(self):
		'''
		GET verb call
		
		Returns a partial template of robots who have checked in.

		Args:
			None	

		Returns:
			table row formated data to be pulled right into a table body.
			
		'''
		bots = database.view("bots/Bots").all()
		botNew = []
		
		for i in bots:
			if i['value']['checkedIn'] is 1:
				botNew.append(i['value'])


		view = scoreboardView.tableView(data=botNew)
		
		return view.returnData()


@baseObject.route('/heat/(.*)/')
class heat(baseObject.baseHTTPObject):
	'''
	Manages views of heats.

	**TODO**: Update this for the new storage of heats in botsDocs not heatDocs
	'''
	def get(self):
		'''
		GET verb call

		Returns a partial template of robots in a heat.

		Args:
			heat - int of the heat number
			
		Returns:
			table row formated data to be pulled right into a table body.
			
		'''
		
		heat = self.hasMember('heat', True)
		
		bots = database.view("bots/Bots").all()

		spots = []

		for bot in bots:
			bot = bot['value']
			if bot['checkedIn']:
				if bot['heatOneWave'] == heat:
					spots.append(bot)
				if bot['heatTwoWave'] == heat:
					spots.append(bot)
				if bot['heatThreeWave'] == heat:
					spots.append(bot)

		view = scoreboardView.heatView(data=spots)
		
		return view.returnData()


@baseObject.route('/admin/')
class admin(baseObject.baseHTTPObject):
	'''
	Just a call to figure out what view to be on
	'''
	def get(self):
		'''
		GET verb call

		returns JSON of which view to be on.
		
		Args:
			None
			
		Returns:
			JSON object silimar to: {"admin": {"viewScreen": "2/1"}} 
			
		'''
		admin = database.view("admin/Admin", key=0).first()['value']

		view = scoreboardView.adminView(data=admin)
		
		return view.returnData()


@baseObject.route('/stand/')
class top3(baseObject.baseHTTPObject):
	'''
	Manages the top3 for ground table
	'''
	def get(self):
		'''
		GET verb call
		
		Returns a partial template of robots who have checked in.

		Args:
			None	

		Returns:
			table row formated data to be pulled right into a table body.
			
		'''
		topType = self.hasMember('type', True)

		bots = database.view("bots/Bots").all()
		'''
		Air Bonuses

		0 - None
		2 - 10 seconds
		3 - 30 seconds
		4 - 10 seconds
		23 - 40 seconds
		24 - 20 seconds

		Ground Bonuses

		1 - 30 seconds
		'''
		bonusTimes = {
			0: datetime.timedelta(seconds=0),
			1: datetime.timedelta(seconds=30),
			2: datetime.timedelta(seconds=10),
			3: datetime.timedelta(seconds=30),
			4: datetime.timedelta(seconds=10),
			23: datetime.timedelta(seconds=40),
			24: datetime.timedelta(seconds=20)
		}

		airTimes = []
		groundTimes = []
		for bot in bots:
			bot = bot['value']
			if bot['checkedIn']:
				times = []
				if bot['heatOneTime'] != '0:00':
					heatOneTime = datetime.datetime.strptime(bot['heatOneTime'], '%M:%S')
					if bot['heatOneBonus']:
						heatOneTime = heatOneTime - bonusTimes[bot['heatOneBonus']]
					times.append(heatOneTime.time())

				if bot['heatTwoTime'] != '0:00':
					heatTwoTime = datetime.datetime.strptime(bot['heatTwoTime'], '%M:%S')
					if bot['heatTwoBonus']:
						heatTwoTime = heatTwoTime - bonusTimes[bot['heatTwoBonus']]
					times.append(heatTwoTime.time())

				if bot['heatThreeTime'] != '0:00':
					heatThreeTime = datetime.datetime.strptime(bot['heatThreeTime'], '%M:%S')
					if bot['heatThreeBonus']:
						heatThreeTime = heatThreeTime - bonusTimes[bot['heatThreeBonus']]
					times.append(heatThreeTime.time())

				if times:
					fastest = min(times)

					if bot['vehicleType'] is 0:
						groundTimes.append({"id": bot['id'], "time":fastest, "_id": bot['_id']})
					else:
						airTimes.append({"id": bot['id'], "time": fastest, "_id": bot['_id']})

		airSorted = sorted(airTimes, key=operator.itemgetter('time'))
		groundSorted = sorted(groundTimes, key=operator.itemgetter('time'))

		air = {}
		if len(airSorted) < 3:
			for i in range(len(airSorted)):
				air.update({(i+1): airSorted[i]})
		else:
			air = {1: airSorted[0], 2: airSorted[1], 3: airSorted[2]}

		ground = {}
		if len(groundSorted) < 3:
			for i in range(len(groundSorted)):
				ground.update({(i+1): groundSorted[i]})
		else:
			ground = {1: groundSorted[0], 2: groundSorted[1], 3: groundSorted[2]}

		for bot in air:
			botData = database.view("bots/Bots", key=air[bot]['id']).first()['value']
			air[bot].update(botData)
		
		for bot in ground:
			botData = database.view("bots/Bots", key=ground[bot]['id']).first()['value']
			ground[bot].update(botData)

#		data = {"air": air, "ground": ground}

		if topType == 'air':
			data = air
		else:
			data = ground

		view = scoreboardView.standView(data=data)
		
		return view.returnData()


app = web.application(baseObject.urls, globals())
