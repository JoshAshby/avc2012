#!/usr/bin/env python2
"""
Official 2012 SparkFun Electronics AVC Scoreboard App

For more information, see: https://github.com/JoshAshby/avc2012e soon

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import couchdbkit
import web
'''
Set this to either:
	gevent
or
	web.py
or
	cgi

To determine the underlying wsgi server for the application.
If set to gevent or standalone, be sure to also change HTTPport
to the port you want to server the main HTTP interface on.
'''
#serverType = 'gevent'
#serverType = 'wsgi'
serverType = 'web.py'

HTTPport = '85'

#Is this going to the live SparkFun server or a dev box?
deploy = True
#deploy = False

#couchdbkit stuff.
databaseName = 'avc'
server = couchdbkit.Server()
database = server.get_or_create_db(databaseName)

#templating stuff
templatesFolder = 'htmlTemplates/'
partialTemplatesFolder = 'htmlTemplates/partials/'

#templating shortcuts... These get passed to templates
#in all the view and template.py files
urlRoot = '/avc'
adminRoot = (urlRoot + '/admin')

if deploy:
	urlRoot = '/avc'
	adminRoot = (urlRoot + '/admin')
	serverType = "web.py"
	#serverType = "wsgi"
	#serverType = "gevent"

assetUrl = '/static'
titleHalf = 'SparkFun 2012 AVC - '

#basic classes that are helpful
class slash:
	def GET(self): raise web.seeother("/")

class static:
	def GET(self,name): return open('static/%s'%name)
