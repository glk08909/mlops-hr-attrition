# Executive Summary
This project focuses on building a machine learning solution to predict employee attrition — whether an employee is likely to leave a company — using historical HR data. The goal is to not only develop an accurate predictive model, but to implement the full machine learning operations (MLOps) pipeline around it.
    The workflow includes:
    •	Ingesting and preprocessing HR employee data
    •	Training and evaluating a classification model
    •	Tracking experiments and model performance with MLflow
    •	Deploying the model via a web service (FastAPI)
    •	Monitoring predictions and setting up workflow orchestration (Prefect)
    •	Ensuring reproducibility, code quality, containerization (Docker), and deployment readiness
The solution leverages the IBM HR Analytics Employee Attrition dataset, containing demographic, employment, and satisfaction-related features for 1470 employees. This predictive system aims to help HR teams identify at-risk employees early, enabling proactive retention strategies and reducing turnover costs.
Ultimately, this project demonstrates how to operationalize a machine learning model using modern MLOps practices, making it scalable, maintainable, and production-ready.

## Problem Description

Project Title: Employee Attrition Prediction using MLOps Pipeline
 
  # Problem Overview:
Employee attrition — when employees voluntarily leave a company — can be costly, disruptive, and detrimental to an organization’s productivity and morale. Being able to predict which employees are at risk of leaving allows HR departments to proactively address issues, retain valuable talent, and reduce recruitment and training expenses.
This project aims to build a machine learning pipeline to predict employee attrition based on historical HR records, using the IBM HR Analytics Employee Attrition dataset.
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

# Objective:
The main objective is to develop an end-to-end, reproducible MLOps workflow that:
•	Ingests employee data
•	Preprocesses and cleans the data
•	Trains a predictive machine learning model
•	Tracks experiments using MLflow
•	Deploys the trained model via a web service
•	Monitors model performance
•	Follows MLOps best practices for reproducibility, version control, containerization, and workflow orchestration

# Dataset Description:
•	Source: IBM HR Analytics Employee Attrition dataset (from Kaggle)
•	Size: 1470 employee records, 35 features
•	Target Variable: Attrition
o	Yes = Employee left the company
o	No = Employee stayed

# Features include:
•	Demographics (Age, Gender, MaritalStatus)
•	Employment history (YearsAtCompany, JobRole, MonthlyIncome)
•	Work-related metrics (JobSatisfaction, WorkLifeBalance, EnvironmentSatisfaction)
 
# Machine Learning Task:
A binary classification problem — predict if an employee will leave (Attrition = 1) or stay (Attrition = 0), based on their profile and work environment attributes.

# Expected Outcome:
•	A trained and logged Random Forest classification model
•	Model performance metrics (accuracy, precision, recall, F1-score)
•	MLflow experiment tracking
•	Dockerized deployment-ready model API (FastAPI)
•	Workflow orchestration using Prefect
•	Clear, reproducible instructions and MLOps best practices in place



# Flow
 ![image](https://github.com/user-attachments/assets/7df04c28-1921-4df2-a5a6-1866a97476f6)

 
# Employee Attrition Prediction API
![image](https://github.com/user-attachments/assets/7c484958-0534-45fb-a31f-52cb2c505061)



# Sample Request object
{
  "Age": 0,
  "BusinessTravel": 0,
  "DailyRate": 0,
  "Department": 0,
  "DistanceFromHome": 0,
  "Education": 0,
  "EducationField": 0,
  "EnvironmentSatisfaction": 0,
  "Gender": 0,
  "HourlyRate": 0,
  "JobInvolvement": 0,
  "JobLevel": 0,
  "JobRole": 0,
  "JobSatisfaction": 0,
  "MaritalStatus": 0,
  "MonthlyIncome": 0,
  "NumCompaniesWorked": 0,
  "OverTime": 0,
  "PercentSalaryHike": 0,
  "PerformanceRating": 0,
  "StockOptionLevel": 0,
  "TotalWorkingYears": 0,
  "TrainingTimesLastYear": 0,
  "WorkLifeBalance": 0,
  "YearsAtCompany": 0,
  "YearsInCurrentRole": 0,
  "YearsSinceLastPromotion": 0,
  "YearsWithCurrManager": 0,
  "StandardHours": 0,
  "JobRoleLevel": 0
}

![Screenshot 2025-07-03 at 9 40 51 PM](https://github.com/user-attachments/assets/12a997c0-401e-4f7d-a2e7-39e497ef49bf)



![Screenshot 2025-07-03 at 8 35 10 PM](https://github.com/user-attachments/assets/ae81f35f-80e6-4f21-b210-793024ba4c9e)



# Response object 
- scenario: The employee is predicted to leave the company.
{
  "attrition_prediction": 1
}


# Response object
- Scenario : The employee is predicted to stay.
{
  "attrition_prediction": 0
}

![Screenshot 2025-07-03 at 8 34 52 PM](https://github.com/user-attachments/assets/ffcafff1-ca95-4041-9fe6-df51618d6ac4)


# Interpretation:
"attrition_prediction" = 1 → The employee is predicted to leave the company.
"attrition_prediction" = 0 → The employee is predicted to stay.
This binary encoding is essential for training classification models like logistic regression, random forests.

# Docker image file.

![Screenshot 2025-07-05 at 12 52 27 PM](https://github.com/user-attachments/assets/41cac48e-df9f-4d3d-88e7-8f89b2938bf7)


![Screenshot 2025-07-05 at 12 49 15 PM](https://github.com/user-attachments/assets/000a9e62-cd71-4074-acf6-8eeac8031eac)

![Screenshot 2025-07-05 at 12 48 51 PM](https://github.com/user-attachments/assets/34ef21e0-47c0-4e51-a293-da7609d26083)

![Screenshot 2025-07-05 at 12 30 42 PM](https://github.com/user-attachments/assets/25f4b059-1ee6-472d-90eb-13a2c6cca7ba)


# ML flow

![Screenshot 2025-07-03 at 7 44 12 PM](https://github.com/user-attachments/assets/9851162b-08f9-4b1c-9939-08444c395f7b)


![Screenshot 2025-07-03 at 7 32 23 PM](https://github.com/user-attachments/assets/d1b598f0-0f2a-4e91-b7e5-6b48c53c860e)



