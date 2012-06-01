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

#set-o-main templates. This is really here for ease of use and so forth
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

#same as above just for partials
partialTemplateSet = {
	'row_listView': (partialTemplatesFolder + 'row_listView.tpl.html'),
	'row_listViewBody': (partialTemplatesFolder + 'row_listViewBody.tpl.html'),
	'row_listAdminView': (partialTemplatesFolder + 'row_listAdminView.tpl.html'),
	'row_listAdminHeatView': (partialTemplatesFolder + 'row_listAdminHeatView.tpl.html'),
}

#generic template class, called by all the views currently
#because nothing fancy is needed.
class genericTemplate(Template):
	baseurl = baseurl
	urlRoot = urlRoot
	asseturl = assetUrl
	title = ''
	content = ''
	checkin = ''

#just one for Partials, not that it's needed, but just as a 
#reminder that your working with a partial. same as above basically.
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

