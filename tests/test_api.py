from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


valid_payload = {
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
}


def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():

    response = client.post(
        "/predict",
        json=valid_payload
    )

    assert response.status_code == 200

    result = response.json()

    assert "predicted_demand" in result
    assert result["predicted_demand"] > 0


def test_invalid_prediction_input():

    invalid_payload = valid_payload.copy()
    invalid_payload["hr"] = 50

    response = client.post(
        "/predict",
        json=invalid_payload
    )

    assert response.status_code == 422