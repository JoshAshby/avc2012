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


class botsDoc(couchdbkit.Document):
	
	barcode = couchdbkit.StringProperty()
	picture = couchdbkit.StringProperty()
	name = couchdbkit.StringProperty()
	doc_type = couchdbkit.StringProperty()
	category = couchdbkit.StringProperty()
	description = couchdbkit.StringProperty()
	flag = couchdbkit.StringProperty()
	
	doc_type = "botsDoc"
	
	quantity = couchdbkit.IntegerProperty()
	rank = couchdbkit.IntegerProperty()
	
	tags = couchdbkit.ListProperty()
	log = couchdbkit.ListProperty()
	
	restock = couchdbkit.DictProperty()
	prediction = couchdbkit.DictProperty()

	def order(self, quantity):
		self.quantity = self.quantity - restockQuantity
		additionalData = {"date": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"), "quantity": self.quantity, "delta": (datetime.datetime.now() - datetime.datetime.strptime(self.restock['date'], "%Y-%m-%d %H:%M:%S")).days(), "norm": (self.quantity / self.restock['quantity'])}
		self.log.append(additionalData)
		self.save()


botsDoc.set_db(database)
