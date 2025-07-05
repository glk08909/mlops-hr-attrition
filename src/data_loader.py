import os
import pandas as pd  # ✅ this line was missing

def load_employee_data(file_path=None):
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, 'data', 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")
    df = pd.read_csv(file_path)
    print(f"[INFO] Data loaded successfully. Shape: {df.shape}")
    return df
