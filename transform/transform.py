import pandas as pd
import yaml

def load_mapping(path='config/mapping.yaml') -> dict:
    return yaml.safe_load(open(path))

def rename_fields(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    return df.rename(columns=mapping['fields'])

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=[c for c in df.columns if c.endswith('_code') or c == 'code'],
                   how='all')
    df = df.drop_duplicates()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()
    return df

def transform(df: pd.DataFrame, entity: str) -> pd.DataFrame:
    mapping = load_mapping()[entity]
    df = rename_fields(df, mapping)
    df = clean(df)
    keep = list(mapping['fields'].values())
    return df[[c for c in keep if c in df.columns]]
