
import os
from pymongo.mongo_client import MongoClient

class MongoClientFactory:

    @staticmethod
    def get_collection_client(db_name,collection_name,host="mongodb",user="",password=""):
        user = user if user else os.getenv("MONGO_INITDB_ROOT_USERNAME")
        password = password if password else os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        host = os.getenv("HOST") if os.getenv("HOST") else host
        
        client = MongoClient(host= host,username= user, password=password)
        db = client[db_name]
        collection = db[collection_name]
        return collection   