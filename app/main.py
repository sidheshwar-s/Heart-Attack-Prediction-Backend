from app.config.logger import LogConfig
from app.model.model import prediction
from fastapi import FastAPI, UploadFile, File
import time

from logging.config import dictConfig
import logging

dictConfig(LogConfig().dict())
logger = logging.getLogger("myapp")


app = FastAPI()

@app.get("/")
def read_root():
    return {"Heart attack prediction": "v0.1.0"}

@app.post("/predict")
async def predict(file: UploadFile):
    logger.info(f"Prediction request is made")
    start_time = time.time()
    pred_res = prediction(file)
    res = pred_res[0]
    end_time = time.time()
    logger.info(f"Prediction result = {res}, time taken for request = {end_time - start_time} sec")
    if res == 0:
        return {"result": 0, "time taken": f"{end_time - start_time} sec"}
    elif res == 1:
        return {"result": 1, "time taken": f"{end_time - start_time} sec"}
    else:
        return {"result": 2, "time taken": f"{end_time - start_time} sec"}
        
