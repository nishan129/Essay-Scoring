from src.essay.logger import logging
from src.essay.pipeline.training_pipeline import TrainingPipeline
from src.essay.entity.config_entity import DataIngestionConfig
from src.essay.utils.comon import read_yaml
from pathlib import Path
import os
if __name__ == '__main__':
    logging.info("Project is starting...")
    train = TrainingPipeline()
    train.run_pipeline()
    logging.info("Project done")