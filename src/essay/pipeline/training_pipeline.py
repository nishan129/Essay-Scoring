from src.essay.components.data_ingestion import DataIngestion
from src.essay.exception import ModelException
from src.essay.logger import logging
from src.essay.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.essay.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:
    def __init__(self) -> None:
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise ModelException(e,sys)
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            return data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise ModelException(e,sys)