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
                mongo_db_url = ""
                MongodbClient.client = pymongo.mongo_client(mongo_db_url,tlsCAFile=ca)
                self.client = MongodbClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
        except Exception as e:
            raise ModelException(e,sys)