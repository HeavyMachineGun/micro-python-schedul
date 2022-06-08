
import os
from models .configuration import Configuration 
from pymongo.mongo_client import MongoClient
from typing import List
from core.client_factory import MongoClientFactory

class SchedulerConfiguration:    
    
    def __init__(self, host= "mongodb") -> None:
        self.collection = MongoClientFactory.get_collection_client(db_name="scheduler_configuration",
        collection_name="configuration")

    
    def get_all_configurations(self) -> List[Configuration]:
        return [Configuration(**item) for item in self.collection.find()]

    def add_configuration(self,configuration:Configuration)-> Configuration:
         self.collection.insert_one(configuration.dict())