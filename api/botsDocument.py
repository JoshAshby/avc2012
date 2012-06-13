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
	builders = couchdbkit.StringProperty()
	
	doc_type = "botDoc"
	
	checkedIn = couchdbkit.IntegerProperty()
	checkedIn = 0
	vehicleType = couchdbkit.IntegerProperty()
	id = couchdbkit.IntegerProperty()
	
	heatOneWave = couchdbkit.StringProperty()
	heatTwoWave = couchdbkit.StringProperty()
	heatThreeWave = couchdbkit.StringProperty()

	heatOneTime = couchdbkit.StringProperty()
	heatTwoTime = couchdbkit.StringProperty()
	heatThreeTime = couchdbkit.StringProperty()

	heatOneBonus = couchdbkit.IntegerProperty()
	heatTwoBonus = couchdbkit.IntegerProperty()
	heatThreeBonus = couchdbkit.IntegerProperty()

botsDoc.set_db(database)
