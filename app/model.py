import pandas as pd
from xgboost import XGBRegressor


MODEL_PATH = "models/bike_demand_xgboost.json"


model = XGBRegressor()
model.load_model(MODEL_PATH)


def is_model_loaded():
    return model is not None


def predict_demand(input_data):
    data = pd.DataFrame([{
        "season": input_data.season,
        "yr": input_data.yr,
        "mnth": input_data.mnth,
        "hr": input_data.hr,
        "holiday": input_data.holiday,
        "weekday": input_data.weekday,
        "workingday": input_data.workingday,
        "weathersit": input_data.weathersit,
        "temp": input_data.temp,
        "atemp": input_data.atemp,
        "hum": input_data.hum,
        "windspeed": input_data.windspeed
    }])

    prediction = model.predict(data)

    return float(prediction[0])