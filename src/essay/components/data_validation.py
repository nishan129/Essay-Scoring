from src.essay.exception import ModelException
from src.essay.logger import logging
from src.essay.constant import *
import os ,sys
from src.essay.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.essay.entity.config_entity import DataValidationConfig
import pandas as pd
from pathlib import Path
from src.essay.utils.comon import read_yaml
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
cmap = mpl.cm.get_cmap('coolwarm') # to add collor and formate of the plot

class DataValidation:
    def __init__(self,data_validation_config =DataValidationConfig, data_ingestion_artifact=DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def check_data_validation(self) -> bool:
        """ To check the data is valid or not and also check the distribution of the data and save the image of the distribution.

        Raises:
            ModelException: To get any erros show the massge 

        Returns:
            bool: The data is valid or not show in True or False
        """
        logging.info("Enter the data validation class")
        try:
            data = pd.read_csv(self.data_ingestion_artifact.feature_store_path)
            value = read_yaml(file_path="scema.yaml")
            
            data_validation_status_path = self.data_validation_config.data_validation_status_path
            data_dir = os.path.dirname(data_validation_status_path)
            os.makedirs(data_dir,exist_ok=True)
            
            logging.info("Check the data columns and data type is same or not")
            # check all collumns and datatype is available in the data 
            for i in range(len(value)):
                if value.columns[i] in data.columns:
                    validation_status = True
                    with open(data_validation_status_path, "a") as f:
                        f.write(f"data columns {value.columns[i]} is {validation_status}. \n")
                        f.close()
                else:
                    validation_status = False
                    with open(data_validation_status_path, "a") as f:
                        f.write(f"data columns {value.columns[i]} is {validation_status}. \n")
                        f.close()
                        
                if value.dtype[i] == data.dtypes[i]:
                    validation_status =True
                    with open(data_validation_status_path ,'a') as f:
                        f.write(f"data dtype {value.dtype[i]} is {validation_status}. \n")
                        f.close()   
                        
                else:
                    validation_status = False
                    with open(data_validation_status_path ,'a') as f:
                        f.write(f"data dtype {value['dtype'][i]} is {validation_status}. \n")
                        f.close()  
                        
            plot_image_path = os.path.dirname(self.data_validation_config.data_validation_plot_dir)
            os.makedirs(plot_image_path,exist_ok=True)
            
            logging.info("Check data distribution ..")
            ## Plot the distribution of the data   
            plt.figure(figsize=(8, 4))
            data.score.value_counts().plot.bar(color=[cmap(0.0), cmap(0.25), cmap(0.65), cmap(0.9), cmap(1.0)])
            plt.xlabel("Score")
            plt.ylabel("Count")
            plt.title("Score distribution for Train Data")
            # Save Seaborn plot as image
            plt.savefig(self.data_validation_config.data_validation_plot_dir+"value_count.png")
            plt.close()
            
            
            plt.figure()
            sns.histplot(data['score'], color='salmon',kde=True, edgecolor='black')  # Add salmon color with black edges
            plt.title('Seaborn Histogram')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
             # Save Seaborn plot as image
            plt.savefig(self.data_validation_config.data_validation_plot_dir+"data_distribution.png")
            plt.close()
            
            logging.info("plot image is saved ")
            return validation_status
        except Exception as e:
            raise ModelException(e,sys)
        
    
    def initiate_data_validation(self) ->DataValidationArtifact:
        try:
            logging.info("Start initiate_data_validation  function on Datavalidation class")
            validation_status = self.check_data_validation()
            data_validation_artifact = DataValidationArtifact(
                status_file_path= self.data_validation_config.data_validation_status_path
            )
            
            logging.info(f"Data validation artifact is {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise ModelException(e,sys)