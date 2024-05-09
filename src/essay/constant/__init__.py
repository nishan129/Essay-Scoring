
ARTIFACTS_DIR : str = "artifacts"


DATABASE_NAME: str = "essay"
COLLECTION_NAME: str = "data"

DATA_NAME = "data.csv"
TRAIN_DATA_NAME = "train.csv"
TEST_DATA_NAME = "test.csv"
DATA_VALIDATION_FILE_NAME = "status.txt"
TOKENIZER_NAME = "tokenizer.pkl"
TRAIN_TRANSFORM_DATA = "train"
TEST_TRANSFORM_DATA = "test"

MODEL_NAM: str = "deberta-v3-small.h5"


MODEL_NAME: str ="microsoft/deberta-v3-xsmall"  #"microsoft/deberta-v3-small"  #"microsoft/deberta-v3-large"

"""
Data ingestion type constant created with constant var name
"""
DATA_INGESTION_COLLECTION_NAME = "data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPILT_RATION: float = 0.2


"""
Data Validation type constant created with constant var name
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_DISTRIBUTION_DIR_NAME: str = "logdir"
DATA_VALIDATION_IMG_SAVE : str = "data_distribution"


"""
Data Transformation type constant created with constant var name
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFOMRED_DATA_DIR_NAME: str = "trasformed_data"


"""
Model Trainer type constant created with constant var name
"""
MODEL_TRAINER_DIR_NAME : str = "train_model"
