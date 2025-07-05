from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# Load model from MLflow registry
model = mlflow.pyfunc.load_model("models:/hr-attrition-model/None")


class EmployeeData(BaseModel):
    Age: int
    MonthlyIncome: float
    JobRole: str
    OverTime: str
    DistanceFromHome: int
    # Add all required fields here...


@app.post("/predict")
def predict(data: EmployeeData):
    df = pd.DataFrame([data.dict()])
    df = pd.get_dummies(df)  # match training preprocessing
    prediction = model.predict(df)
    return {"Attrition": bool(prediction[0])}
