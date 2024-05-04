from src.essay.constant import *
from src.essay.entity.config_entity import DataTransformationConfig
from src.essay.entity.artifact_entity import DataTransformationArtifact, DataIngestionArtifact
from src.essay.logger import logging
from src.essay.exception import ModelException
import os,sys
import pandas as pd
from src.essay.ml.tokenizer import Tokeinze
from transformers import AutoTokenizer
from tokenizers import AddedToken
from src.essay.utils.comon import save_model


class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise ModelException(e, sys)
        
    def transformed_data(self):
        """ To transform data and save data and tokenizer

        Raises:
            ModelException: To got errors in model exception form
        """
        logging.info("Enter the data transformation class")
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.training_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            
            tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
            tokenizer.add_tokens([AddedToken("\n", normalized=False)])
            tokenizer.add_tokens([AddedToken(" "*2, normalized=False)])
            
            tokenize = Tokeinze(train_df, test_df, tokenizer)
            
            tokenized_train, tokenized_test, tokenizer_model = tokenize()
            
            
            """ Save train transformed data in train path """
            
            train_path = self.data_transformation_config.train_transform_data
            train_dir = os.path.dirname(train_path)
            os.makedirs(train_dir,exist_ok=True)
            
            tokenized_train.save_to_disk(train_path)
            logging.info(f"Saved Train transformed data in train path{train_path}")
            
            """ Save test transformed data in test path """
            test_path = self.data_transformation_config.test_trainsform_data
            test_dir = os.path.dirname(test_path)
            os.makedirs(test_dir, exist_ok= True)
            
            tokenized_test.save_to_disk(test_path)
            logging.info(f"Saved Test transformed data in test path{test_path}")
            
            """ Save Tokenizer in transformed path """
            tokenizer_path = self.data_transformation_config.data_transformed_data_dir
            tokenizer_dir = os.path.dirname(tokenizer_path)
            
            os.makedirs(tokenizer_dir, exist_ok=True)
            save_model(file_path=tokenizer_path, model=tokenizer_model)
            
        except Exception as e:
            raise ModelException(e, sys)
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            self.transformed_data()
            data_transform_artifact = DataTransformationArtifact(
                train_data_path=self.data_transformation_config.train_transform_data,
                test_data_path=self.data_transformation_config.test_trainsform_data,
                tokenizer_file_path=self.data_transformation_config.data_transformed_data_dir
            )
            return data_transform_artifact
        except Exception as e:
            raise ModelException(e, sys)
    