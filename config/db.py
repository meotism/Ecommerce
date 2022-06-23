#import mongoClient
from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        pass

    def get_db(self):
        url = "mongodb+srv://meotism:Mewtism1@cluster0.iqxih.mongodb.net/nhayenanhxuan?retryWrites=true&w=majority"
        database_name = "nhayenanhxuan"
        client = MongoClient(url)
        db = client[database_name]
        print("connect success")
        return db
