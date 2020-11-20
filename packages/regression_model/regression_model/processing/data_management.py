import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
import os

from config import config

def load_dataset(*,file_name: str) -> pd.DataFrame:
    _data = pd.read_csv(f"{config.DATASET_DIR}\{file_name}")
    return _data

def save_pipeline(*,pipeline_to_persist) -> None:
    """Pipeline to persist"""

    save_file_name = "rf_regression_model.pkl"
    save_path = os.path.join(config.TRAINED_MODEL_DIR,save_file_name)
   
    joblib.dump(pipeline_to_persist,save_path)
        
    print("pipeline saved...")


def load_pipeline(*,file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = os.path.join(config.TRAINED_MODEL_DIR,file_name)
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline