import pandas as pd

def extract_data(csv_path: str):
    df = pd.read_csv(csv_path, encoding='utf-8-sig')
    return df