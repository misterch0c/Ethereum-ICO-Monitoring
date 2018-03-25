import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

from pyetherscan import Client
etherScanClient = Client()
#pyeth=pyetherscan.ethereum

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.db

div=1000000000000000000
icos = db.icos


#Updates balance of all addresses
def updateBalanceAll():
	for ico in icos.find():
		thisBalance=etherScanClient.get_single_balance(ico["address"]).balance/div
		thisName=ico["name"]
		print(thisName)
		print(thisBalance)
		icos.update({"name":thisName},{"$set":{"balance":thisBalance}})		

updateBalanceAll()
