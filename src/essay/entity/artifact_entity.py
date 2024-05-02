from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    training_file_path : Path
    test_file_path : Path