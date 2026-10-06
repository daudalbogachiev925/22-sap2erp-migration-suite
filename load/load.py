import pandas as pd
from sqlalchemy import create_engine, text

def upsert(df: pd.DataFrame, table: str, key: str, engine):
    with engine.begin() as conn:
        for _, row in df.iterrows():
            cols = ', '.join(row.index)
            vals = ', '.join(f":{c}" for c in row.index)
            updates = ', '.join(f"{c}=EXCLUDED.{c}" for c in row.index if c != key)
            sql = f"""INSERT INTO {table} ({cols}) VALUES ({vals})
                      ON CONFLICT ({key}) DO UPDATE SET {updates}"""
            conn.execute(text(sql), row.to_dict())
    print(f"Загружено в {table}: {len(df)}")

def load_all(data: dict, engine):
    if 'customers' in data: upsert(data['customers'], 'clients', 'code', engine)
    if 'materials' in data: upsert(data['materials'], 'products', 'sku', engine)
    if 'orders'    in data: upsert(data['orders'], 'orders', 'number', engine)
