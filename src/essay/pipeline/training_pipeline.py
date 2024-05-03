from src.essay.components.data_ingestion import DataIngestion
from src.essay.exception import ModelException
from src.essay.logger import logging
from src.essay.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
from src.essay.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact
from src.essay.components.data_validation import DataValidation
import sys


class TrainingPipeline:
    def __init__(self) -> None:
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise ModelException(e,sys)
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Start data ingestion ")
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("End data ingestion")
            return data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            logging.info("Start data validation")
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"End data validation {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise ModelException(e,sys)