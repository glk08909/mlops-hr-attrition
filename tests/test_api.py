import requests


def test_prediction_endpoint():
    url = "http://127.0.0.1:8010/predict"
    payload = {
        "Age": 30,
        "MonthlyIncome": 5000,
        "JobRole": "Research Scientist",
        "OverTime": "Yes",
        "DistanceFromHome": 10,
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "Attrition" in response.json()
