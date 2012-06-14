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
import web
import listPage
import scoreboardPage
import standPage
import adminPage
import teamPage
import aboutPage

if not deploy:
	web.config.debug = True

urls = (
	(urlRoot + '/list'), listPage.app,
	(urlRoot + '/scoreboard'), scoreboardPage.app,
	(urlRoot + '/stand'), standPage.app,
	(urlRoot + '/about'), aboutPage.app,
	(urlRoot + '/admin'), adminPage.app,
	'/static/(.*)', 'static'
)
