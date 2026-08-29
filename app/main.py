from fastapi import FastAPI

from app.schemas import BikeDemandInput
from app.model import predict_demand,is_model_loaded


app = FastAPI(
    title="Bike Demand Prediction API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bike Demand Prediction API."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded":is_model_loaded()
    }


@app.post("/predict")
def predict(input_data: BikeDemandInput):

    prediction = predict_demand(input_data)

    return {
        "predicted_demand": prediction
    }