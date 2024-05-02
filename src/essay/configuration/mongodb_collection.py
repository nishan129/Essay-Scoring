import os,sys

import pymongo.mongo_client
from src.essay.logger import logging
from src.essay.exception import ModelException
from src.essay.constant import *
import pymongo
import certifi

ca = certifi.where()

class MongodbClient:
    client = None
    
    
    def __init__(self,database_name=DATABASE_NAME) -> None:
        
        try:
            if MongodbClient.client is None:
                mongo_db_url = "mongodb+srv://nishantborkar139:Lata12@cluster0.p4fnk6s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
                MongodbClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
                self.client = MongodbClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
        except Exception as e:
            raise ModelException(e,sys)