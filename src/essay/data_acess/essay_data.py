import sys
from typing import Optional

import numpy as np
import pandas as pd

from src.essay.configuration.mongodb_collection import MongodbClient
from src.essay.exception import ModelException
from src.essay.logger import logging
from src.essay.constant import *

class ExtractData:
    """
    This class export all mongodb data as pandas data frame
    """
    
    def __init__(self):
        try:
            self.mongodb_client = MongodbClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise ModelException(e,sys)
        
    def export_collection_as_dataframe(self,
                                       collection_name:str, database_name: Optional[str] = None) -> pd.DataFrame:
        """ Export Entire collection as dataframe
        returns pd.DataFrame as collection

        Args:
            collection_name (str): collection_name is the mongodb data collection name ex. Data
            database_name (Optional[str], optional): datavase_name is a mongodb data base name where database collection is exist. Defaults to None.

        Returns:
            pd.DataFrame: ruturn data as dataframe formate
        """
        try:
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id","essay_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            
            
            return df
        except Exception as e:
            raise ModelException(e,sys)