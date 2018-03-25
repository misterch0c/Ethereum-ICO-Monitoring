import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

from pyetherscan import Client
etherScanClient = Client()
pyeth=pyetherscan.ethereum
address="0xE28e72FCf78647ADCe1F1252F240bbfaebD63BcC"
address_balance = etherScanClient.get_single_balance(address)
print(address_balance.balance/1000000000000000000000)

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.db
icos = db.eth
div=1000000000000000000

#for ico  in icos.find():
#	pprint.pprint(ico)
#pprint.pprint(icos.find_one({"name":"DigiDAO"}))

