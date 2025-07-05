from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI(
    title="Employee Attrition Prediction API",
    description="Predicts employee attrition using a trained Random Forest model.",
    version="1.0.0",
)

# Load trained model
model = joblib.load("src/models/random_forest_model.joblib")


# Define request body structure
class EmployeeData(BaseModel):
    Age: int
    BusinessTravel: int
    DailyRate: int
    Department: int
    DistanceFromHome: int
    Education: int
    EducationField: int
    EnvironmentSatisfaction: int
    Gender: int
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: int
    JobSatisfaction: int
    MaritalStatus: int
    MonthlyIncome: int
    NumCompaniesWorked: int
    OverTime: int
    PercentSalaryHike: int
    PerformanceRating: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int
    StandardHours: int
    JobRoleLevel: int


@app.post("/predict")
def predict(data: EmployeeData):
    try:
        input_data = np.array(
            [
                [
                    data.Age,
                    data.BusinessTravel,
                    data.DailyRate,
                    data.Department,
                    data.DistanceFromHome,
                    data.Education,
                    data.EducationField,
                    data.EnvironmentSatisfaction,
                    data.Gender,
                    data.HourlyRate,
                    data.JobInvolvement,
                    data.JobLevel,
                    data.JobRole,
                    data.JobSatisfaction,
                    data.MaritalStatus,
                    data.MonthlyIncome,
                    data.NumCompaniesWorked,
                    data.OverTime,
                    data.PercentSalaryHike,
                    data.PerformanceRating,
                    data.StockOptionLevel,
                    data.TotalWorkingYears,
                    data.TrainingTimesLastYear,
                    data.WorkLifeBalance,
                    data.YearsAtCompany,
                    data.YearsInCurrentRole,
                    data.YearsSinceLastPromotion,
                    data.YearsWithCurrManager,
                    data.StandardHours,
                    data.JobRoleLevel,
                ]
            ]
        )

        print(f"Input data shape: {input_data.shape}")
        print(model.feature_names_in_)

        prediction = model.predict(input_data)
        return {"prediction": int(prediction[0])}

    except Exception as e:
        return {"error": str(e)}
