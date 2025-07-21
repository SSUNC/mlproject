#packages required
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.Utils import save_object
from src.logger import logging
from src.exception import CustomException

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transform_data():
        '''
        Function is responsible for data transformation
        '''
        try:
            numerical_columns=["writing_score", "reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='media')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[('imputer',SimpleImputer(strategy='most_frequent')),
                       ('scaler',StandardScaler(with_mean=False)),
                       ('one_hot_encoder',OneHotEncoder())
                        ]
            )

            logging.info(f"categorical columns:{categorical_columns}")
            logging.info(f"numerical columns:{numerical_columns}")

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
            ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)