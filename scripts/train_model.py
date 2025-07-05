import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("HR Attrition")

# Load your dataset
df = pd.read_csv("notebooks/hr_attrition.csv")  # Replace with your actual dataset path
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# One-hot encode categorical features
X = pd.get_dummies(X)

# Convert target to binary if it's not already
if y.dtype == 'object':
    y = y.map({'Yes': 1, 'No': 0})


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start MLflow run
with mlflow.start_run():
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log parameters and metrics
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", acc)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print(f"✅ Model logged with accuracy: {acc:.4f}")
