import pymongo
import random
import datetime
import time

myclient = pymongo.MongoClient("mongodb://192.168.80.131:27010/")
mydb = myclient["stock"]
mycol = mydb["stock_detail"]

price = random.randint(5,10)
tick_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
msg = "time:{},sid:{},sname:{},price:{}".format(tick_time, 11, "bata", price)
print(msg)
for i in mycol.find({},{"_id":0}):
    print(i)