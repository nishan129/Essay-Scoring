import yaml
import os, sys
from src.essay.logger import logging
from src.essay.exception import ModelException
from pathlib import Path
from box import ConfigBox

def read_yaml(file_path:Path) -> ConfigBox:
    try:
        logging.info(f"Read yaml file: {file_path}")
        with open(file_path, "r") as f:
            return ConfigBox(yaml.safe_load(f))
    except Exception as e:
        raise ModelException(e,sys)