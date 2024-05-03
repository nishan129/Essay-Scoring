from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    training_file_path : Path
    test_file_path : Path
    feature_store_path : Path
    
@dataclass
class DataValidationArtifact:
    status_file_path : Path