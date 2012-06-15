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
	'standView': (templatesFolder + 'standView.tpl.html'),
	'standViewBody': (templatesFolder + 'standViewBody.tpl.html'),
	'adminMainView': (templatesFolder + 'adminMainView.tpl.html'),
	'adminTeamListView': (templatesFolder + 'adminTeamListView.tpl.html'),
	'adminTeamView': (templatesFolder + 'adminTeamView.tpl.html'),
	'adminTeamAirView': (templatesFolder + 'adminTeamAirView.tpl.html'),
	'adminTeamNewView': (templatesFolder + 'adminTeamNewView.tpl.html'),
	'adminScoreboardView': (templatesFolder + 'adminScoreboardView.tpl.html'),
	'adminHeatListView': (templatesFolder + 'adminHeatListView.tpl.html'),
	'adminHeatEditView': (templatesFolder + 'adminHeatEditView.tpl.html'),
	'adminHeatBotView': (templatesFolder + 'adminHeatBotView.tpl.html'),
	'adminHeatBotBodyView': (templatesFolder + 'adminHeatBotBodyView.tpl.html'),
	'adminHeatNewView': (templatesFolder + 'adminHeatNewView.tpl.html'),
	'aboutView': (templatesFolder + 'about.tpl.html'),
	'scoreboardView': (templatesFolder + 'scoreboard.tpl.html'),
}

#same as above just for partials
partialTemplateSet = {
	'row_listView': (partialTemplatesFolder + 'row_listView.tpl.html'),
	'row_listViewBody': (partialTemplatesFolder + 'row_listViewBody.tpl.html'),
	'row_listAdminHeatBodyView': (partialTemplatesFolder + 'row_listAdminHeatBodyView.tpl.html'),
	'row_listStandView': (partialTemplatesFolder + 'row_standView.tpl.html'),
	'row_listStandViewBody': (partialTemplatesFolder + 'row_standViewBody.tpl.html'),
	'row_listAdminView': (partialTemplatesFolder + 'row_listAdminView.tpl.html'),
	'row_listAdminHeatView': (partialTemplatesFolder + 'row_listAdminHeatView.tpl.html'),
	'row_listAdminHeatBotView': (partialTemplatesFolder + 'row_listAdminHeatBotView.tpl.html'),
	'row_listAdminHeatBotBodyView': (partialTemplatesFolder + 'row_listAdminHeatBotBodyView.tpl.html'),

}

#generic template class, called by all the views currently
#because nothing fancy is needed.
class genericTemplate(Template):
	urlRoot = urlRoot
	adminRoot = adminRoot
	asseturl = assetUrl
	title = ''
	content = ''
	checkin = ''

#just one for Partials, not that it's needed, but just as a 
#reminder that your working with a partial. same as above basically.
class PartialListRow(Template):
	urlRoot = urlRoot
	adminRoot = adminRoot
	asseturl = assetUrl
	title = ''
	teamId = ''
	botName = ''
	teamName = ''
	builders = ''
	checkin = ''

