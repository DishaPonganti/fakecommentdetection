from pymongo import MongoClient

def getDbConnection():
    # create a Mongoclient
    client = MongoClient()

    # connect your client to local instance
    db = client['local']

    return db