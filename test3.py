import pymongo
data =[
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://sourav1894:Svthegreat2803@cluster0.wsu5p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory'] #database created
collection = database['table'] #collection is like table in SQL
#collection.insert_many(data)

#search operations
#d = collection.find({'status': 'A'})
#d = collection.find({'status': {'$in':['A', 'P']}})
#d = collection.find({'status': {'$gt': "C"}})
#d = collection.find({'qty': {'$gte': 75}}) #gte = greater than or equal to
#d = collection.find({'item': 'sketch pad', 'qty': 95}) #query on multiple columns #AND condition
#d = collection.find({'item': 'sketch pad', 'qty': {'$gte': 75}})
#d = collection.find({'$or':[{'item': 'sketch pad'}, {'qty': {'$gte': 75}}]}) #OR condition

#UPDATE Operation
#collection.update_one({'item': 'canvas'}, {'$set': {'item': 'sourav'}})
#d = collection.find({'item': 'sourav'})

#DELETE Operation
#collection.delete_one({'item': 'sourav'})
d = collection.find({'item': 'sourav'})
for i in d:
    print(i)



