import pandas as pd
from sqlalchemy import create_engine

def compare_counts(source_df: pd.DataFrame, target_table: str, engine):
    target_df = pd.read_sql(f"SELECT * FROM {target_table}", engine)
    return {
        'source_rows': len(source_df),
        'target_rows': len(target_df),
        'match': len(source_df) == len(target_df),
        'diff': len(source_df) - len(target_df)
    }

def compare_sums(source_df: pd.DataFrame, target_table: str, field: str, engine):
    target_df = pd.read_sql(f"SELECT SUM({field}) AS s FROM {target_table}", engine)
    return {
        'source_sum': float(source_df[field].astype(float).sum()),
        'target_sum': float(target_df['s'].iloc[0] or 0)
    }

def find_missing(source_df: pd.DataFrame, target_table: str, key: str, engine):
    target_df = pd.read_sql(f"SELECT {key} FROM {target_table}", engine)
    missing = set(source_df[key]) - set(target_df[key])
    return list(missing)
