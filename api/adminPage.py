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
import adminView
import baseObject
from adminDocument import *
from botsDocument import *
from heatDocument import *

baseObject.urlReset()


@baseObject.route('/')
class adminMain(baseObject.baseHTTPObject):
	'''
	Displays the main admin landing page.
	'''
	def get(self):
		'''
		GET verb call
		
		returns the template for the admin landing page,
		nothing fancy here just a few links to the areas.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		view = adminView.adminMainView()
		
		return view.returnData()


@baseObject.route('/scoreboard/')
class adminScoreboard(baseObject.baseHTTPObject):
	'''
	Manages the current view on the over all scoreboard
	'''
	def get(self):
		'''
		GET verb call
		
		Displays the template with the 6 buttons corrisponding
		to which scoreboard view should be shown.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heats = database.view("schedule/Schedule").all()
		heatNew = []

		for i in heats:
			heatNew.append({"id": i['value']['_id'], "num": i['value']['heat']})

		view = adminView.adminScoreboardView()
		
		return view.returnData()

	def post(self):
		'''
		POST verb call

		updates the admin doc to reflect a change in the view

		Args:
			view - Can be any of: 0,1,2,2/1,3,3/1

		Returns:
			Nothing, error page if something went wrong.
		'''
		nextView = str(self.hasMember('view', True))

		docId = database.view("admin/Admin", key=0).first()['value']['_id']

		doc = adminDoc.get(docId)

		doc.viewScreen = nextView
		doc.save()
		

@baseObject.route('/teams/')
class adminTeamList(baseObject.baseHTTPObject):
	'''
	Manages the team list
	'''
	def get(self):
		'''
		GET verb call
		
		generates a list of all the robots and then places
		them into a table in the template.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		bots = database.view("bots/Bots").all()
		botNew = []
		
		for i in bots:
			botNew.append(i['value'])

		view = adminView.adminTeamListView(data=botNew)
		
		return view.returnData()

	def post(self):
		'''
		POST verb call
		
		Marks the given botId number as checked in
		
		Args:
			botId - just an int representing the robots id number

		Returns:
			Nothing, error page if somethings wrong

		'''
		botId = str(self.hasMember('botId', True))

		docId = database.view("bots/Bots", key=0).first()['value']['_id']

		doc = botsDoc.get(docId)

		doc.checkedIn = 1

		doc.save()


@baseObject.route('/team/(.*)/')
class adminTeam(baseObject.baseHTTPObject):
	'''
	Manages a teams info.
	'''
	def get(self):
		'''
		GET verb call
		
		pulls the teams info from the database and places it in the template
		
		Args:
			botId - just an int representing the robots ID in the database
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		bot = int(self.hasMember('botId', True))

		doc = database.view("bots/Bots", key=bot).first()['value']

		heats = database.view("schedule/Schedule").all()
		heatNew = []

		for i in heats:
			heatNew.append({"id": i['value']['_id'], "num": i['value']['heat']})

		data={"bot": doc, "heat": heatNew}

		view = adminView.adminTeamView(data=data)
		
		return view.returnData()

	def post(self):
		'''
		POST verb call
		
		Updates the given information in the database

		Args:
			botId - int
			name - str
			builders - str
			checkedIn - int, one or zero
			team - str
			vehicleType - int, one for air, zero for air
			location - str
			heatOne - str of the database doc _id
			heatTwo - str of the database doc _id
			heatThree - str of the database doc _id

		Returns:
			Nothing, error page if somethings wrong

		'''
		botId = int(self.hasMember(0))

		docId = database.view("bots/Bots", key=botId).first()['value']['_id']
		doc = botsDoc.get(docId)

		name = self.hasMember('name')
		builders = self.hasMember('builders')
		checkedIn = self.hasMember('checkedIn')
		team = self.hasMember('team')
		vehicleType = self.hasMember('vehicleType')
		location = self.hasMember('location')
		heatOne = self.hasMember('heatOne')
		heatTwo = self.hasMember('heatTwo')
		heatThree = self.hasMember('heatThree')

		if name: doc.name = str(name)
		if builders: doc.builders = str(builders)
		if checkedIn: doc.checkedIn = int(checkedIn)
		if team: doc.team = str(team)
		if vehicleType: doc.vehicleType = int(vehicleType)
		if location: doc.location = str(location)
		
		# Next up we're going to store the id # of the 
		# heat doc which holds the info for that heat.
		# This way it's easy to pull out all three heats
		# when looking at one robot, and still about to be
		# used to concoct a set of bots for each id number.
		if heatOne:
			doc.heatOne = str(heatOne)

		if heatTwo:
			doc.heatTwo = str(heatTwo)

		if heatThree:
			doc.heatThree = str(heatThree)

		doc.save()

	def put(self):
		'''
		PUT verb call
		
		Inserts a new team into the database.
		This *should* work...

		Args:
			name - str
			builders - str
			checkedIn - int, one or zero
			team - str
			vehicleType - int, one for air, zero for air
			location - str
			heatOne - str of the database doc _id
			heatTwo - str of the database doc _id
			heatThree - str of the database doc _id

		Returns:
			Nothing, error page if somethings wrong

		'''
		botIds = []
		bots = database.view("bots/Bots")
		for bot in bots:
			botIds.append(bot['value']['id'])

		doc = botsDoc(id=(max(botIds)+1))

		name = self.hasMember('name')
		builders = self.hasMember('builders')
		checkedIn = self.hasMember('checkedIn')
		team = self.hasMember('team')
		vehicleType = self.hasMember('vehicleType')
		location = self.hasMember('location')
		heatOne = self.hasMember('heatOne')
		heatTwo = self.hasMember('heatTwo')
		heatThree = self.hasMember('heatThree')

		if name: doc.name = str(name)
		if builders: doc.builders = str(builders)
		if checkedIn: doc.checkedIn = int(checkedIn)
		if team: doc.team = str(team)
		if vehicleType: doc.vehicleType = int(vehicleType)
		if location: doc.location = str(location)
		
		# Next up we're going to store the id # of the 
		# heat doc which holds the info for that heat.
		# This way it's easy to pull out all three heats
		# when looking at one robot, and still about to be
		# used to concoct a set of bots for each id number.
		if heatOne:
			doc.heatOne = str(heatOne)

		if heatTwo:
			doc.heatTwo = str(heatTwo)

		if heatThree:
			doc.heatThree = str(heatThree)

		doc.save()

		
@baseObject.route('/heat/')
class adminHeatList(baseObject.baseHTTPObject):
	'''
	Manages the heats

	**TODO**: Add a PUT verb call to add new heats
	'''
	def get(self):
		'''
		GET verb call

		returns a template of all the heats, pulled from the botDocs
		and compiled into a complete list.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heats = database.view("schedule/Schedule")

		view = adminView.adminHeatView(data=heats)
		
		return view.returnData()

@baseObject.route('/heat/new/')
class adminHeatNew(baseObject.baseHTTPObject):
	'''
	Manages the new heats

	'''
	def get(self):
		'''
		GET verb call

		returns a template of all the heats, pulled from the botDocs
		and compiled into a complete list.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heats = database.view("schedule/Schedule")

		view = adminView.adminHeatView(data=heats)
		
		return view.returnData()

	def post(self):
		'''
		POST ver call

		returns nothing unless something goes wronge
		(in which case it'll give an error page).

		Args:
			
		Returns:
			Nothing, as stated above.
		'''
		time = self.hasMember("time")
		vehicleType = self.hasMember("vehicleType")

		docId = database.view("schedule/Schedule").last()['value']

		doc = heatDoc.get(heat=docId['heat']+1)
		
		doc.time = time
		doc.vehicleType = int(vehicleType)

		doc.save()


@baseObject.route('/heat/(.*)/')
class adminHeatInfo(baseObject.baseHTTPObject):
	'''
	Manages info for each heat

	'''
	def get(self):
		'''
		GET verb call

		returns a template of all the heats, pulled from the botDocs
		and compiled into a complete list.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heatId = int(self.hasMember("heatId", True))

		heat = database.view("schedule/Schedule", key=heatId).first()['value']

		view = adminView.adminHeatEditView(data=heat)
		
		return view.returnData()


	def post(self):
		'''
		POST verb call

		updates the heats info, but not which bots are competing.
		Bots that are in that heat are managed through the botsDoc
		because of how heats are setup, a little more work and complication
		but with limited time thats how it has to be, sorry guys.

		Args:
			heatId - int of the heat number
			time - duh.
			vehicleType - int, one for air, zero for ground

		Returns:
			Nothing, error page if somethings wrong.

		'''
		heatId = int(self.hasMember("heatId", True))
		time = self.hasMember("time")
		vehicleType = self.hasMember("vehicleType")

		docId = database.view("schedule/Schedule", key=heatId).first()['value']['_id']
		doc = heatDoc.get(docId)
		
		if time:
			doc.time = time
		else:
			doc.vehicleType = int(vehicleType)

		doc.save()


@baseObject.route('/heat/bots/')
class adminHeatBotList(baseObject.baseHTTPObject):
	'''
	Manages robots in each of the heats

	'''
	def get(self):
		'''
		GET verb call

		returns a template of all the heats, pulled from the botDocs
		and compiled into a complete list of which robot and which heat.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heats = {}
		bots = database.view("bots/Bots")
		for bot in bots:
			heats.update({bot['value']['heatOne']: []})
			heats.update({bot['value']['heatTwo']: []})
			heats.update({bot['value']['heatThree']: []})

		for bot in bots:
			heats[bot['value']['heatOne']].append(bot['value'])
			heats[bot['value']['heatTwo']].append(bot['value'])
			heats[bot['value']['heatThree']].append(bot['value'])

		view = adminView.adminHeatBotListView(data=heats)
		
		return view.returnData()

@baseObject.route('/heat/bots/(.*)/')
class adminHeatBotInfo(baseObject.baseHTTPObject):
	'''
	Manages robots in each of the heats

	'''
	def get(self):
		'''
		GET verb call

		returns a template of all the heats, pulled from the botDocs
		and compiled into a complete list of which robot and which heat.
		
		Args:
			None
			
		Returns:
			HTML template, see adminView and templates.py for more info.
			
		'''
		heatId = self.hasMember("heatId", True)

		heats = {}
		bots = database.view("bots/Bots")
		for bot in bots:
			heats.update({bot['value']['heatOne']: []})
			heats.update({bot['value']['heatTwo']: []})
			heats.update({bot['value']['heatThree']: []})

		for bot in bots:
			heats[bot['value']['heatOne']].append(bot['value'])
			heats[bot['value']['heatTwo']].append(bot['value'])
			heats[bot['value']['heatThree']].append(bot['value'])

		heat = heats[heatId]

		view = adminView.adminHeatBotInfoView(data=heat)
		
		return view.returnData()

app = web.application(baseObject.urls, globals())
