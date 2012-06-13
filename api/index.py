#!/usr/bin/env python2
"""
Official 2012 SparkFun Electronics AVC Scoreboard App

For more information, see: https://github.com/JoshAshby/avc2012

**WARNING**
Make sure you look through and change things in configSub.py
before running this file, to be sure it runs the way you want it to

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import sys, os

try:
	from configSub import *
except:
	abspath = os.path.dirname(__file__)
	sys.path.append(abspath)
	os.chdir(abspath)
	from configSub import *

if serverType is 'gevent':
	from gevent import monkey; monkey.patch_all()
	from gevent.pywsgi import WSGIServer

import web
import json
from config import *
import baseObject
import indexView

baseObject.urlReset()


@baseObject.route(urlRoot + '/')
class index(baseObject.baseHTTPObject):  
	'''
	Base index view, nothing fancy just a landing page
	'''
	def get(self):
		'''
		GET verb call

		returns the index template which is just a fancy landing page.

		Args:
			None

		Returns:
			HTML template; see indexView.py and templates.py for more info.

		'''
		view = indexView.indexView()
		return view.returnData()


urls += baseObject.urls

if __name__ == "__main__":
	print "Herewego!"
	print "I'll give you a nice list of all the URLs I'm serving things on..."
	print urls
	print 'Now serving py on port %s with the %s library...' % (HTTPport, serverType)
	if serverType is 'gevent':
		app = web.application(urls, globals())
		app.internalerror = web.debugerror
		WSGIServer(('', int(HTTPport)), app.wsgifunc()).serve_forever()
	if serverType is 'cgi':
		app = web.application(urls, globals())
		app.internalerror = web.debugerror
		main = app.wsgifunc()
		application = app.wsgifunc()
	else:
		if HTTPport: sys.argv.append(HTTPport)
		app = web.application(urls, globals())
		app.internalerror = web.debugerror
		app.run()
