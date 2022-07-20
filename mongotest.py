import pymongo
client = pymongo.MongoClient("mongodb+srv://Shahiraj555:Nikita12345@cluster0.9zrun.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# db = client.test
# print(db)
db1=client['mongotest']
coll=db1['test']

d = {
    'name':'shahiraj',
    'email':'shahirajlakade555@gmail.com',
    'surname': 'Lakade'
}

coll.insert_one(d)




