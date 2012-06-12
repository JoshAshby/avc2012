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
#serverType = 'web.py'
serverType = 'web.py standalone'

HTTPport = '80'

#couchdbkit stuff.
databaseName = 'avc'
server = couchdbkit.Server()
database = server.get_or_create_db(databaseName)

#templating stuff
templatesFolder = 'htmlTemplates/'
partialTemplatesFolder = 'htmlTemplates/partials/'

#templating shortcuts... These get passed to templates
#in all the view and template.py files
baseurl = '/avc2012/api'
urlRoot = '/avc'
assetUrl = '/static'
titleHalf = 'SparkFun 2012 AVC - '

