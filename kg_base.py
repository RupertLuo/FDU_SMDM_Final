import pymongo

client = pymongo.MongoClient('127.0.0.1',port = 27017)
db = client.douban
collection = db.movies
result = collection.find({'id':'26387939'})
for i in result:
    print(i)

