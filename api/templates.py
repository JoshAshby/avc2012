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
	'listViewBody': (templatesFolder + 'listViewBody.tpl.html'),
	'adminMainView': (templatesFolder + 'adminMainView.tpl.html'),
	'adminTeamListView': (templatesFolder + 'adminTeamListView.tpl.html'),
	'adminTeamView': (templatesFolder + 'adminTeamView.tpl.html'),
	'adminScoreboardView': (templatesFolder + 'adminScoreboardView.tpl.html'),
	'adminScheduleView': (templatesFolder + 'adminScheduleView.tpl.html'),
	'aboutView': (templatesFolder + 'about.tpl.html'),
	'scoreboardView': (templatesFolder + 'scoreboard.tpl.html'),
}

partialTemplateSet = {
	'row_listView': (partialTemplatesFolder + 'row_listView.tpl.html'),
	'row_listViewBody': (partialTemplatesFolder + 'row_listViewBody.tpl.html'),
	'row_listAdminView': (partialTemplatesFolder + 'row_listAdminView.tpl.html'),
}

class genericTemplate(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	asseturl = assetUrl
	title = ''
	content = ''

class PartialListRow(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	asseturl = assetUrl
	title = ''
	teamId = ''
	botName = ''
	teamName = ''
	builders = ''
	checkin = ''

