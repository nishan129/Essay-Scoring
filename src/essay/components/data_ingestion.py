from src.essay.logger import logging
from src.essay.exception import ModelException
from src.essay.entity.config_entity import DataIngestionConfig
from src.essay.entity.artifact_entity import DataIngestionArtifact
from src.essay.data_acess.essay_data import ExtractData
from src.essay.constant import *
from sklearn.model_selection import train_test_split

import os, sys
import pandas as pd


class DataIngestion:
    def __init__(self, data_ingestion_config = DataIngestionConfig):
        try:
            
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ModelException(e,sys)
    
    def extract_data_into_feature_store(self) -> pd.DataFrame:
        """ To extract data from mongodb and save data as pandas data frame

        Returns:
            pd.DataFrame: To save data as pandas dataframe
        """
        try:
            logging.info("Exporting data from mongodb to feature store")
            mognodb_databse = ExtractData()
            data = mognodb_databse.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_stor_file_path = self.data_ingestion_config.feature_store_path
            
            dir_path = os.path.dirname(feature_stor_file_path) # to get directory name
            os.makedirs(dir_path, exist_ok=True) # to create a directory
            data.to_csv(feature_stor_file_path,index=False,header=True)
            
            logging.info("Exporting data from mongodb is complete")
            return data
        except Exception as e:
            raise ModelException (e,sys)
        
    def split_data(self, data: pd.DataFrame) ->None:
        try:
            logging.info("Splitting data in to Train and Test format is start..")
            train_data, test_data = train_test_split(data, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=True)
            train_data_path = self.data_ingestion_config.training_file_path
            test_data_path = self.data_ingestion_config.test_file_path
            
            train_dir_path = os.path.dirname(train_data_path)
            test_dir_path = os.path.dirname(test_data_path)
            os.makedirs(train_dir_path, exist_ok=True)
            os.makedirs(test_dir_path,exist_ok=True)
            
            train_data.to_csv(train_data_path,index=False,header=True)
            test_data.to_csv(test_data_path,index=False,header=True)

            logging.info("Splitting data in to Train and Test is complete")
        except Exception as e:
            raise ModelException(e,sys)
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data = self.extract_data_into_feature_store()
            self.split_data(data)
            
            data_ingestion_artifact = DataIngestionArtifact(
                training_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            
            return data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)