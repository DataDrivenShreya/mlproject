## Read the data with Tain and Test Split 

# Import libraries
import os 
import sys 
from src.exception import CustomException 
from src.logger import logging 
import pandas as pd 

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 

# Create Folder and File name 
@dataclass 
class DataIngestionConfig:
    train__data_path: str=os.path.join('artifact',"train.csv")
    test__data_path: str=os.path.join('artifact',"test.csv")
    raw__data_path: str=os.path.join('artifact',"raw.csv")

# Make Train and Test Split
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the data 
            df= pd.read_csv(r'C:\Users\shrey\mlproject\notebook\data\student.csv')
            logging.info('Read the dataset as dataframe')

            # Make folder 
            os.makedirs(os.path.dirname(self.ingestion_config.train__data_path),exist_ok=True)
            
            # Data into Raw datafolder
            df.to_csv(self.ingestion_config.raw__data_path,index=False,header=True)

            # Train and Test Split 
            logging.info("Train Test Split Initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)

            # Move train and test data into their folder
            train_set.to_csv(self.ingestion_config.train__data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test__data_path,index=False,header=True)
        
            logging.info("Ingestion of the data is completed")

            # Return Train and Test Path 
            return (
                self.ingestion_config.train__data_path,
                self.ingestion_config.test__data_path,

            )
        except Exception as e:
            raise CustomException(e,sys) 
        
if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
