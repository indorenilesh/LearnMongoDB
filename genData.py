'''

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("192.168.80.131", 27010)
db=client["AIPL"]
collection = db["employee"]
db.collection.find()
data = collection.find()
pprint(data)

'''

import pymongo
import random
import datetime
import time

myclient = pymongo.MongoClient("mongodb://192.168.80.131:27010/")
mydb = myclient["stock"]
mycol = mydb["stock_detail"]

def genTick(sid,sname,minprice,maxprice):
    price = random.randint(minprice, maxprice)
    tick_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = {'time':tick_time,'sid':sid,'sname':minprice,'price':maxprice}
    return(msg)

while True:
    for i in mycol.find({},{"_id":0}):
        currentTick=genTick(i["s_id"],i["s_name"],int(i["s_min"]),int(i["s_max"]))
        mynewcol = mydb["tick_data"]
        mynewcol.insert_one(dict(currentTick))
    time.sleep(5)
