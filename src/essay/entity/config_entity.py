from src.essay.constant import *
import os, sys 
from pathlib import Path
from dataclasses import dataclass


@dataclass
class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir: str = ARTIFACTS_DIR
   

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        
        self.feature_store_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR,DATA_NAME)
        self.training_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_DATA_NAME)
        self.test_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_DATA_NAME)
        
        self.train_test_split_ratio : float = DATA_INGESTION_TRAIN_TEST_SPILT_RATION
        self.collection_name: str = DATA_INGESTION_COLLECTION_NAME
        