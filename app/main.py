from fastapi import FastAPI
import pandas as pd

from app.schemas import PredictionInput
from app.predictor import predict_sales

app = FastAPI()

@app.get("/")

def home():
    return {"message":"sales forecasting api"}

@app.post("/predict")
def predict(data: PredictionInput):

    df = pd.DataFrame([data.model_dump()])

    prediction = predict_sales(df)

    return {
        "predicted_sales": float(prediction[0])
    }