import pandas as pd

def mask_card(card_number: str) -> str:
    digits = str(card_number).replace('-', '').replace(' ', '')
    if len(digits) >= 4:
        return '****-****-****-' + digits[-4:]
    return str(card_number)

def transform_data(df: pd.DataFrame):
    data = df.copy()

    data['Nome'] = data['Nome'].astype(str).str.strip().str.title()
    data['Conta'] = data['Conta'].astype(str).str.strip()
    data['Cartão'] = data['Cartão'].astype(str).str.strip().apply(mask_card)

    data = data.drop_duplicates()

    return data