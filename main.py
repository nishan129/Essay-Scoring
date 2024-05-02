from src.essay.logger import logging
from src.essay.pipeline.training_pipeline import TrainingPipeline
from src.essay.entity.config_entity import DataIngestionConfig

if __name__ == '__main__':
    logging.info("Project is starting...")
    data = TrainingPipeline()
    data.run_pipeline()