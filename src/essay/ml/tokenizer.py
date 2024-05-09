from datasets import Dataset
from src.essay.exception import ModelException
from src.essay.logger import logging
import sys

class Tokeinze(object):
    
    def __init__(self,train,test,tokenizer) -> None:
        try:
            self.train = train
            self.test = test
            self.tokenizer = tokenizer
        except Exception as e:
             raise ModelException(e,sys)
        
    def get_dataset(self, df):
        try:
            ds = Dataset.from_dict({
                "full_text": [tf for tf in df['full_text']],
                'label': [s for s in df['label']],
            })
            
            return ds
        except Exception as e:
            raise ModelException(e,sys)
    
    def tokenize_function(self, example):
        try:
            tokenize_input = self.tokenizer(
                example['full_text'],truncation=True, max_length=1024
            )
            
            return tokenize_input
        except Exception as e:
            raise ModelException(e,sys)
        
    def __call__(self):
        try:
            train_ds = self.get_dataset(self.train)
            test_ds = self.get_dataset(self.test)
            
            tokenized_train = train_ds.map(
                self.tokenize_function, batched=True
            )
            
            tokenized_test = test_ds.map(self.tokenize_function, batched=True)
            
            return tokenized_train, tokenized_test, self.tokenizer
        except Exception as e:
            raise ModelException(e,sys)