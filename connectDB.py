import pymongo


myclient = pymongo.MongoClient("mongodb://192.168.80.131:27010/")
mydb = myclient["stock"]
mycol = mydb["stock_detail"]

#mycol.remove()

'''
stock_dict1 = {"s_id":"11","s_name":"bata","s_min":"50","s_max":"60"}
stock_dict2 = {"s_id":"12","s_name":"tata","s_min":"2100","s_max":"2300"}
stock_dict3 = {"s_id":"13","s_name":"mahindra","s_min":"950","s_max":"1150"}
stock_dict4 = {"s_id":"14","s_name":"lnt","s_min":"280","s_max":"350"}
stock_dict5 = {"s_id":"15","s_name":"cisco","s_min":"1200","s_max":"1350"}
'''

'''
mycol.insert_one(stock_dict2)
mycol.insert_one(stock_dict3)
mycol.insert_one(stock_dict4)
mycol.insert_one(stock_dict5)
'''

#print(mycol.find_one())

'''
for i in mycol.find():
    print(i)
'''
'''
stock_list = [{"s_id":"16","s_name":"disco","s_min":"70","s_max":"110"},{"s_id":"17","s_name":"infosys","s_min":"1600","s_max":"1750"},{"s_id":"18","s_name":"capgemini","s_min":"800","s_max":"900"},{"s_id":"19","s_name":"tcs","s_min":"1000","s_max":"1100"},{"s_id":"20","s_name":"ags","s_min":"10","s_max":"15"}]
mycol.insert_many(stock_list)
'''

'''
for i in mycol.find():
    print(i)
'''

'''
for i in mycol.find({},{"s_id":1}):
    print(i)
'''
#try:
#    print(mydb.list_collection_names())
#except:
#    print("DB is down!!!!")


#print(myclient.list_database_names())

for i in mycol.find({"s_id":"12"},{"_id":0}):
    print(i)
