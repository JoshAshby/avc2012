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
import web
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
serverType = 'gevent'

HTTPport = 80

databaseName = 'avc'
database = couchdbkit.Server()[databaseName]

templatesFolder = 'public/'

render = web.template.render(templatesFolder)

class slash:
	def GET(self): raise web.seeother("/")
