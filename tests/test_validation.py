import pytest
from pydantic import ValidationError

from app.schemas import BikeDemandInput


def test_valid_input():

    data = BikeDemandInput(
        season=4,
        yr=1,
        mnth=10,
        hr=17,
        holiday=0,
        weekday=2,
        workingday=1,
        weathersit=1,
        temp=0.62,
        atemp=0.60,
        hum=0.50,
        windspeed=0.10
    )

    assert data.hr == 17


def test_invalid_hour():

    with pytest.raises(ValidationError):

        BikeDemandInput(
            season=4,
            yr=1,
            mnth=10,
            hr=50,
            holiday=0,
            weekday=2,
            workingday=1,
            weathersit=1,
            temp=0.62,
            atemp=0.60,
            hum=0.50,
            windspeed=0.10
        )