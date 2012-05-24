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


class baseView(object):
	def __init__(self, **kwargs):
		self.data = kwargs['data']
		
		self.t = 'json'
		
		if 'wi' in kwargs:
			if 't' in kwargs['wi']: self.t = kwargs['wi']['t']
		
		if self.t == 'html':
			self.inform = self.HTML()
		elif self.t == 'json':
			self.inform = self.JSON()
	
	def PDF(self):
		pass
		
	def HTML(self):
		pass
		
	def JSON(self):
		pass
	
	def returnData(self):
		return self.inform