import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import warnings
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os
import sys
from src.utils import save_obj, evaluate_models

@dataclass
class ModelTrainerConfig:
  trained_model_file_path=os.path.join("artifacts", "models.pkl")

class ModelTrainer:
  def __init__(self):
    self.model_trainer_config=ModelTrainerConfig()
  def initiate_model_trainer(self, train_arr, test_arr):
    try:
      logging.info("Splitting training and test input data")
      X_train = train_arr[:, :-1]
      y_train = train_arr[:, -1]

      X_test = test_arr[:, :-1]
      y_test = test_arr[:, -1]
      
      models = {
        "Linear Regression": LinearRegression(),
        "Lasso": Lasso(),
        "Ridge": Ridge(),
        "K-Neighbors Regressor": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest Regressor": RandomForestRegressor(),
        "XGBRegressor": XGBRegressor(),
        "CatBoostRegressor": CatBoostRegressor(verbose=0),
        "AdaBoostRegressor": AdaBoostRegressor()
      }
      model_report:dict=evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)
      best_model_score=max(sorted(model_report.values()))
      best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
      best_model=models[best_model_name]
      if best_model_score<0.6:
        raise CustomException("No best model found")
      logging.info("Best Model found for training and testing dataset...")
      save_obj(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)
      predicted=best_model.predict(X_test)
      r2_scored=r2_score(y_test, predicted)
      return r2_scored


    except Exception as e:
      raise CustomException(e, sys)

