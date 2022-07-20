import pymongo

client = pymongo.MongoClient("mongodb+srv://sourav1894:Svthegreat2803@cluster0.wsu5p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name": "sourav",
    "email": "sourav1894@gmail.com",
    "surname": "bal"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)