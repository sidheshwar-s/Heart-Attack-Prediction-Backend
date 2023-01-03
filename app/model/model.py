import pickle
from pathlib import Path
import pandas as pd
from fastapi import UploadFile

_version = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict = True).parent

with open(f"{BASE_DIR}/trained_model-{_version}.pkl", "rb") as f:
    model = pickle.load(f)

def prediction(file: UploadFile):
    data = pd.read_csv(file.file)
    X = data.iloc[:,:-1]
    Y = data.iloc[:,-1]
    return model.predict(X)