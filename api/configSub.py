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

'''
Set this to either:
	gevent
or
	web.py
	
To determine the underlying wsgi server for the application.
If set to gevent, be sure to also change HTTPport to the port
you want to server the main HTTP interface on.
'''
#serverType = 'gevent'
serverType = 'web.py'

HTTPport = 80

databaseName = 'avc'
server = couchdbkit.Server()
database = server.get_or_create_db(databaseName)

templatesFolder = 'htmlTemplates/'
partialTemplatesFolder = 'htmlTemplates/partials/'
#templating shortcuts...
baseurl = '/avc2012/api'
urlRoot = '/avc'
assetUrl = '/static'
titleHalf = 'SparkFun 2012 AVC - '

class slash:
	def GET(self): raise web.seeother("/")

class static:
	def GET(self,name): return open('static/%s'%name)
