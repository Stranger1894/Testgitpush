import pymongo

client = pymongo.MongoClient("mongodb+srv://sourav1894:Svthegreat2803@cluster0.wsu5p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['myinfo'] #database created
collection = database['test'] #collection is like table in SQL

"""record = collection.find() #search operation
for i in record:
    print(i)
"""

"""data = collection.find({"companyName": "iNeuron"})
for i in data:
    print(i)"""

"""data1 = collection.find({"courseOffered": {"$gt": "E"}}) #gt = greater than #$ is initiation of query
for i in data1:
    print(i)"""

