import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data(df):
    df = df.dropna()

    # Separate target
    y = df["Attrition"]
    X = df.drop("Attrition", axis=1)

    # Identify categorical columns (object dtype)
    cat_cols = X.select_dtypes(include=["object"]).columns

    # One-hot encode categorical columns
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    # Train-test split with stratify
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(
        f"preprocess_data returned: {X_train.shape[0]}, {X_test.shape[0]}, {y_train.shape[0]}, {y_test.shape[0]}"
    )
    return X_train, X_test, y_train, y_test
