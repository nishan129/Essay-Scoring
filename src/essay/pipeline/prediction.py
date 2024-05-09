import pandas as pd
from src.essay.ml.tokenizer import Tokeinze
from src.essay.logger import logging
from src.essay.exception import ModelException
from src.essay.constant import *
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorWithPadding
from src.essay.entity.config_entity import CGF
import sys
from tokenizers import AddedToken
import numpy as np

training_args = TrainingArguments(
                output_dir="./results",
                fp16=True,
                learning_rate=CGF.lr,
                per_device_train_batch_size=CGF.train_batch_size,
                per_device_eval_batch_size=CGF.eval_batch_size,
                num_train_epochs=CGF.train_epochs,
                weight_decay=CGF.weight_decay,
                evaluation_strategy='epoch',
                metric_for_best_model='qwk',
                save_strategy='epoch',
                save_total_limit=1,
                load_best_model_at_end=True,
                report_to='none',
                warmup_ratio=CGF.warmup_ratio,
                lr_scheduler_type='linear', # "cosine" or "linear" or "constant"
                optim='adamw_torch',
                logging_first_step=True,
            )

class Predict:
    def __init__(self, data:pd.DataFrame):
        self.data = data
        
        
    def predict(self):
        try:
            self.data['label'] = 0.0
            
            tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            tokenizer.add_tokens([AddedToken("\n", normalized=False)])
            tokenizer.add_tokens([AddedToken(" "*2, normalized=False)])
            
            
            tokenize = Tokeinze(self.data, self.data, tokenizer)
            data, _ ,_ = tokenize()
            
            data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
            
            model = AutoModelForSequenceClassification.from_pretrained("artifacts/train_model")
            
            trainer = Trainer(
                         model=model,
                        args=training_args,
                        train_dataset=data,
                        data_collator=data_collator,
                        tokenizer=tokenizer,
                                    )
            
            predictions = trainer.predict(data).predictions
            
            preds = np.mean(predictions, axis=0)
            
            score = preds.clip(0,5).round(0)+1
            
            return score 
        except Exception as e:
            raise ModelException(e,sys)


