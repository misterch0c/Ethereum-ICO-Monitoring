import pymongo
import pprint
import sched, time
from pymongo import MongoClient
from bson.objectid import ObjectId
from pyetherscan import Client
from twython import Twython

etherScanClient = Client()
#pyeth=pyetherscan.ethereum

#######################################
twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.db
div=1000000000000000000
icos = db.icos
s = sched.scheduler(time.time, time.sleep)

#######################################

#Updates balance of all addresses
def updateBalanceAll():
	for ico in icos.find():
		thisBalance=etherScanClient.get_single_balance(ico["address"]).balance/div
		thisName=ico["name"]
		icos.update({"name":thisName},{"$set":{"balance":thisBalance}})		

updateBalanceAll()

#Compare actual balance with the one saved in the db every x time
def checkBalances(sc): 
	for ico in icos.find():
		currentBalance=etherScanClient.get_single_balance(ico["address"]).balance/div
		if(ico["balance"]!=currentBalance):
			#balance has changed
			#post a tweet
			twitter.update_status(status=ico["name"]+" ether balance has changed from "+ico["balance"]+ "$eth to "+currentBalance+ "$eth => https://etherscan.io/address/" + ico["address"] )
			#update new balance
			icos.update({"name":ico["name"]},{"$set":{"balance":currentBalance}})

	#2 seconds for testing
    s.enter(2, 1, do_something, (sc,))

s.enter(2, 1, do_something, (s,))
s.run()