#Auhtor: @misterch0c

import pymongo
import pprint
import sched, time
from pymongo import MongoClient
from bson.objectid import ObjectId
from pyetherscan import Client
from twython import Twython

#######################################
APP_KEY=""
APP_SECRET=""
OAUTH_TOKEN=""
OAUTH_TOKEN_SECRET=""
twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
etherScanClient = Client()
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



#Compare actual balance with the one saved in the db every x time
def checkBalances(): 
	print("checking balances")
	for ico in icos.find():
		currentBalance=etherScanClient.get_single_balance(ico["address"]).balance/div
		#we only tweet if balance is decreasing
		if(ico["balance"]!=currentBalance):
			print("Balance has changed, updating db")
			icos.update({"name":ico["name"]},{"$set":{"balance":currentBalance}})
		if((ico["balance"]-currentBalance)>=200):
			print("Balance of " + ico["name"] + " decreased")
			twitter.update_status(status=ico["name"]+" ether balance has decreased from "+str(round(ico["balance"],2))+ " $eth to "+str(round(currentBalance,2))+ " $eth => https://etherscan.io/address/" + ico["address"] )
			

	#2 seconds for testing
	s.enter(600, 1, checkBalances)

#updateBalanceAll()
s.enter(600, 1, checkBalances)
s.run()