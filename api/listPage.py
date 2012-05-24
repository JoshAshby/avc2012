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
import web
import json
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from configSub import *
from botsDocument import *
from picture import *
import listView
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class all(baseObject.baseHTTPObject):
	'''

	'''
	def get(self):
		'''
		GET verb call
		
		
		Args:
			
		Returns:
			
		'''
		bots = database.view("bots/all").all()
		
		for i in bots:
			i = i['value']
		
		view = listView.botsInfoView(data=bots)
		
		return view.returnData()
		
	def post(self):
		'''
		POST verb call
		
		Args:
			
		Returns:
			
		'''
		bar = self.hasMember('bot')

		picTrue = self.hasMember('picTrue', True)
		if picTrue: pictureTrue = int(picTrue)
		else: pictureTrue = None
		pic = self.hasMember('picture', True)
		
		if pictureTrue is not None:
			catdog = re.search('(\..*)', pic.filename).group()
			
			frodo = bar + catdog
			
			f = open(abspath + '/pictures/' + frodo, "wb")

			while 1:
				chunk = pic.file.read(10000)
				if not chunk:
					break
				f.write( chunk )
			f.close()
			
			goop = Pics(frodo)
			goop.Thumb()
			product.picture = frodo



app = web.application(baseObject.urls, globals())