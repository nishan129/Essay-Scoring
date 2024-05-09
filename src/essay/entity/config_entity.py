from src.essay.constant import *
import os, sys 
from pathlib import Path
from dataclasses import dataclass


@dataclass
class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir: str = ARTIFACTS_DIR
   
@dataclass
class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        
        self.feature_store_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR,DATA_NAME)
        self.training_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_DATA_NAME)
        self.test_file_path: str = os.path.join(self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_DATA_NAME)
        
        self.train_test_split_ratio : float = DATA_INGESTION_TRAIN_TEST_SPILT_RATION
        self.collection_name: str = DATA_INGESTION_COLLECTION_NAME
        
        
@dataclass
class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_validation_dir: str = os.path.join(self.training_pipeline_config.artifact_dir,DATA_VALIDATION_DIR_NAME)
        self.data_validation_status_path: str = os.path.join(self.data_validation_dir,DATA_VALIDATION_FILE_NAME)
        self.data_validation_plot_dir: str = os.path.join(self.data_validation_dir,DATA_DISTRIBUTION_DIR_NAME,DATA_VALIDATION_IMG_SAVE)
        
        
        
@dataclass
class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_transformation_dir = os.path.join(self.training_pipeline_config.artifact_dir,DATA_TRANSFORMATION_DIR_NAME)
        self.train_transform_data: str = os.path.join(self.data_transformation_dir,TRAIN_TRANSFORM_DATA)
        self.test_trainsform_data: str = os.path.join(self.data_transformation_dir,TEST_TRANSFORM_DATA)
        self.data_transformed_data_dir: str = os.path.join(self.data_transformation_dir,DATA_TRANSFOMRED_DATA_DIR_NAME,TOKENIZER_NAME)
        
        
@dataclass
class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.model_trainer_dir :str = os.path.join(self.training_pipeline_config.artifact_dir,MODEL_TRAINER_DIR_NAME)
        self.train_model_path : str= os.path.join(self.model_trainer_dir,MODEL_NAM)
        
@dataclass      
class CGF:
    n_splits = 5
    seed = 42
    max_length = 1024
    lr = 1 #1e-5
    train_batch_size = 1
    eval_batch_size = 1
    train_epochs = 4
    weight_decay = 0.01
    warmup_ratio = 0.0
    num_labels = 6