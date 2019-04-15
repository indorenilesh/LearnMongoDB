import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.80.131:27010/")
#mydb = myclient["stock"]
#mycol = mydb["stock_detail"]

#Insert single line data
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#mycol.insert_one({"Name":"Nilesh","Age":35})

#Insert multiple line data
#mylist = [
#{"Name":"A1","Age":21},
#{"Name":"A2","Age":22},
#{"Name":"A3","Age":23},
#{"Name":"A4","Age":24},
#{"Name":"A5","Age":25},
#{"Name":"A6","Age":26},
#{"Name":"A7","Age":27},
#{"Name":"A8","Age":28},
#{"Name":"A9","Age":29},
#{"Name":"A10","Age":30}
#]
#x = mycol.insert_many(mylist)
#print(x.inserted_ids)


#To retrieve single line
#x = mycol.find_one()

#To retrieve whole collection or multiple lines
#for i in mycol.find():
#    print(i)

#Output with selective field
#for i in mycol.find({},{"s_name":1,"s_id":1,"_id":0}):
#    print(i)

#get data for particular age
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery = { "Age" : { "$gt"  : 30 }}
#myoutput = mycol.find(myquery)
#for x in myoutput:
#    print(x)

#get specific data
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery = { "Age" : { "$lt"  : 30 }}
#myoutput = mycol.find(myquery)
#for x in myoutput:
#    print(x)

#Sort data
#mycol = mydb["tick_data"]
#myoutput = mycol.find().sort("price")  # for descending use mycol.find().sort("price",-1)
#for x in myoutput:
#    print(x)

#Delete single line
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery={"Name":"A2"}
#mycol.delete_one(myquery)

#Delete multiple lines
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery={"Name": {"$regex":"^A"}}
#x = mycol.delete_many(myquery)
#print(x.deleted_count, " documents deleted.")

#Delete all documents in a collection
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#x = mycol.delete_many({})
#print(x.deleted_count, " documents deleted.")

#Update single collection
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery = {"s_name" : "dell"}
#newvalues = { "$set" : { "s_name" : "bell" }}
#mycol.update_one(myquery,newvalues)

#Update multiple collection
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myquery = {"s_name" : { "$regex" : "^h" }}
#newvalue={ "$set" : { "s_name" : "HCompany" }}
#x = mycol.update_many(myquery,newvalue)
#print(x.modified_count, " documents updated.")

#Limit the result
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#myresult = mycol.find().limit(5)
#for i in myresult:
#    print(i)

#Delete collection
#mydb = myclient["AIPL"]
#mycol = mydb["employee"]
#mycol.drop()

