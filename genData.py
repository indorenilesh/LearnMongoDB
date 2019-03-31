from pymongo import MongoClient
from pprint import pprint

client = MongoClient("192.168.80.131", 27010)
db=client["AIPL"]
collection = db["employee"]
db.collection.find()
data = collection.find()
pprint(data)