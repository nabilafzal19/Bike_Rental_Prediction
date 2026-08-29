import pandas as pd

from xgboost import XGBRegressor


MODEL_PATH = "models/bike_demand_xgboost.json"


def test_model_prediction():
    model = XGBRegressor()
    model.load_model(MODEL_PATH)

    input_data = pd.DataFrame([{
        "season": 4,
        "yr": 1,
        "mnth": 10,
        "hr": 17,
        "holiday": 0,
        "weekday": 2,
        "workingday": 1,
        "weathersit": 1,
        "temp": 0.62,
        "atemp": 0.60,
        "hum": 0.50,
        "windspeed": 0.10
    }])

    prediction = model.predict(input_data)[0]

    assert prediction > 0