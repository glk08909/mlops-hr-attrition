import joblib
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

def train_and_log_model(X_train, X_test, y_train, y_test):
    # Start MLflow experiment
    mlflow.set_experiment("Employee_Attrition_Prediction")

    with mlflow.start_run():
        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predict & evaluate
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"[INFO] Accuracy: {acc:.4f}")
        print(classification_report(y_test, preds))

        # Log parameters, metrics, model to MLflow
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "random_forest_model")

        os.makedirs("models", exist_ok=True)
        # Save model locally
        joblib.dump(model, "models/random_forest_model.joblib")
        print("[INFO] Model saved locally in 'models/'")
        print("Current working directory:", os.getcwd())