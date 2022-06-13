from pymongo import MongoClient
import json
from bson.json_util import dumps, loads

client = MongoClient("mongodb://localhost:27017")

print(client.list_database_names())

db = client['test-mongo']

print(db.list_collection_names())

users = db['users']
userIds= map(lambda user: user['_id'], db['users'].find())

for userId in list(userIds):
    userCollection = users.find_one({'_id': userId})
    j = dumps(userCollection).replace('22', '333')
    users.replace_one({'_id': userId}, loads(j))
    print(j)
    

# j = dumps(list(users))

# j = j.replace('22', '333')


# print(j)
