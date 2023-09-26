import pymongo

client = pymongo.MongoClient("mongodb+srv://rajsrm81:tdfOSr1FjqcLuDHr@cluster0.iaytpvb.mongodb.net/?retryWrites=true&w=majority")

db = client.test
print(db)

d = {
    "Name":'Ajay',
    "email":'abc@gmail.com',
    'surname':'kumar'
}

db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d)