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
import baseObject
import datetime
import operator
import standView

baseObject.urlReset()


@baseObject.route('/')
class all(baseObject.baseHTTPObject):
	'''
	Manages the heavy lifting of whos the top 3 and who won what.
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
		print database
		try:
			bots = database.view("bots/Bots").all()
		except:
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
			"0": datetime.timedelta(seconds=0),
			"1": datetime.timedelta(seconds=30),
			"2": datetime.timedelta(seconds=10),
			"3": datetime.timedelta(seconds=30),
			"4": datetime.timedelta(seconds=10),
			"23": datetime.timedelta(seconds=40),
			"24": datetime.timedelta(seconds=20)
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

		data = {"air": air, "ground": ground}
		view = standView.listView(data=data)
		
		return view.returnData()


app = web.application(baseObject.urls, globals())
