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


class adminDoc(couchdbkit.Document):
	
	doc_type = "adminDoc"
	
	heat = couchdbkit.StringProperty()
	heat = ''
	wave = couchdbkit.StringProperty()
	wave = ''
	waveId = couchdbkit.StringProperty()
	waveId = ''

	heatNext = couchdbkit.StringProperty()
	heatNext = ''
	waveNext = couchdbkit.StringProperty()
	waveNext = ''
	waveNextId = couchdbkit.StringProperty()
	waveNextId = ''

	viewScreen = couchdbkit.StringProperty()
	viewScreen = ''


adminDoc.set_db(database)
