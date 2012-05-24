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

mainTemplateSet = {
	'index': (templatesFolder + 'index.tpl.html'),
	'listView': (templatesFolder + 'listView.tpl.html'),
	'adminMainView': (templatesFolder + 'admin.tpl.html')
}

partialTemplateSet = {
	'row_listView': (partialTemplatesFolder + 'row_listView.tpl.html')
}

class indexTemplate(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	title = ''

class listViewTemplate(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	title = ''
	content = ''

class adminMainView(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	title = ''
	content = ''

class PartialListRow(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	teamId = ''
	botName = ''
	teamName = ''
	builders = ''

