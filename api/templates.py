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
from Cheetah.Template import Template

templateSet = {
	'index': (templatesFolder + 'index.tpl.html'),
	'listView': (templatesFolder + 'listView.tpl.html')
}

class indexTemplate(Template):
	baseurl = '/'
	title = 'SparkFun AVC 2012 Scoreboard'
	