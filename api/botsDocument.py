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
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from configSub import *


class botsDoc(couchdbkit.Document):
	
	name = couchdbkit.StringProperty()
	team = couchdbkit.StringProperty()
	location = couchdbkit.StringProperty()
	description = couchdbkit.StringProperty()
	builders = couchdbkit.StringProperty()
	
	doc_type = "botsDoc"
	
	checkedIn = couchdbkit.IntegerProperty()
	vehicleType = couchdbkit.IntegerProperty()
	id = couchdbkit.IntegerProperty()
	
	heats = couchdbkit.DictProperty()

	heats = {
		"1": {
			"time": 0,
			"corners": 0,
			"bonus": {
				"langBox": 0,
				"landLot": 0,
				"takeOff": 0,
				"ring": 0,
				},
		},
		"2": {
			"time": 0,
			"corners": 0,
			"bonus": {
				"langBox": 0,
				"landLot": 0,
				"takeOff": 0,
				"ring": 0,
				},
	},
		"3": {
			"time": 0,
			"corners": 0,
			"bonus": {
				"langBox": 0,
				"landLot": 0,
				"takeOff": 0,
				"ring": 0,
				},
		},
	}

botsDoc.set_db(database)
