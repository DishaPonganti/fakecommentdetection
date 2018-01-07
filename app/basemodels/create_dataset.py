import pymongo
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.local
new_collection = db['comments_dataset']

db_data = db.electronics_dataset.find().limit(2000)

for rec in db_data:
    new_collection.save(rec)

