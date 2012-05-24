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
import sys, os
from config import *
import baseObject
import indexView

baseObject.urlReset()


@baseObject.route(urlRoot + '/')
class index(baseObject.baseHTTPObject):  
	'''
	Base Index
	
	'''
	def get(self):
		view = indexView.indexView()
		return view.returnData()

urls += baseObject.urls

if __name__ == "__main__":
	print "Heres the URLs I'm serving things on..."
	print urls
	if serverType is 'gevent':
		from gevent import monkey; monkey.patch_all()
		from gevent.pywsgi import WSGIServer
		app = web.application(urls, globals()).wsgifunc()
		app.internalerror = web.debugerror
		print 'Now serving py on port %i...' % (HTTPport)
		WSGIServer(('', HTTPport), app).serve_forever()
	else:
		app = web.application(urls, globals())
		app.internalerror = web.debugerror
		app.run()
