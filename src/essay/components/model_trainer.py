from src.essay.logger import logging
from src.essay.exception import ModelException
from src.essay.utils.comon import save_model, load_model
from src.essay.entity.config_entity import ModelTrainerConfig, CGF
from src.essay.constant import *
from src.essay.entity.artifact_entity import ModelTrainerArtifact, DataTransformationArtifact
import os, sys
from transformers import  AutoModelForSequenceClassification, AutoConfig, BitsAndBytesConfig
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorWithPadding
from src.essay.ml.metrix import compute_metrics_for_regression
import tensorflow as tf
from datasets import Dataset
import torch






class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig, data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def train_model(self):
        try:
            logging.info("Model Trainer is starting...")
            
            path_dir = os.path.dirname(self.model_trainer_config.train_model_path)
            print("path",path_dir)
            os.makedirs(path_dir, exist_ok=True)
            device = "cuda" if torch.cuda.is_available() else "cpu" 
            
            tokenized_train = Dataset.load_from_disk(self.data_transformation_artifact.train_data_path)
        #     print(tokenized_train)
            tokenized_test = Dataset.load_from_disk(self.data_transformation_artifact.test_data_path)
            
            tokenizer = load_model(self.data_transformation_artifact.tokenizer_file_path)
            config = AutoConfig.from_pretrained(MODEL_NAME)
            config.attention_probs_dropout_prob = 0.0 
            config.hidden_dropout_prob = 0.0 
            config.num_labels = 1  
            
        #     # bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4",bnb_4bit_compute_dtype=torch.bfloat16)
        #     # bnb_config.num_labels = CGF.num_labels 
            model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, config=config)
            
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

            model.resize_token_embeddings(len(tokenizer))
            
        #     # quantize(model, weights=torch.int8, activations=None)
            
            model.gradient_checkpointing_enable()
        #     #model = prepare_model_for_kbit_training(model)
            
        #     #config = LoraConfig(r=8,lora_alpha=32,target_modules=["classifier"],lora_dropout=0.05,bias="none",task_type="classification")
            
        #     #model = get_peft_model(model, config)
            data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
            
            trainer = Trainer( 
            model=model,
            args=training_args,
            train_dataset=tokenized_train,
            eval_dataset=tokenized_test,
            data_collator=data_collator,
            tokenizer=tokenizer,
            compute_metrics=compute_metrics_for_regression,
           # callbacks = [tensorboard]
        )
            
            trainer.train()
            
            
            
            model.save(self.model_trainer_config.train_model_path)
            
            logging.info("Model Train Successfully")
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def initiate_trainer(self):
        try:
            self.train_model()
        except Exception as e:
            raise ModelException(e,sys)