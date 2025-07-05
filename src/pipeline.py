import data_loader
import preprocess
import train_model
from prefect import flow, task
import os
from prefect import task


@task
def load_data_task():
    data = data_loader.load_employee_data()
    return data


@task
def preprocess_data_task(data):
    X_train, X_test, y_train, y_test = preprocess.preprocess_data(data)
    print(
        f"preprocess_data returned: {len(X_train)}, {len(X_test)}, {len(y_train)}, {len(y_test)}"
    )
    return X_train, X_test, y_train, y_test


@task
def train_model_task(X_train, X_test, y_train, y_test):
    train_model.train_and_log_model(X_train, X_test, y_train, y_test)


@flow(name="Employee Attrition ML Pipeline")
def employee_attrition_pipeline():
    data = load_data_task()
    X_train, X_test, y_train, y_test = preprocess_data_task(data)
    train_model_task(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    employee_attrition_pipeline()


@task
def ensure_dirs():
    os.makedirs("models", exist_ok=True)
    os.makedirs("mlruns", exist_ok=True)
