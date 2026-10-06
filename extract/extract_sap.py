import pandas as pd

def extract_from_csv(path: str, table: str) -> pd.DataFrame:
    """Заглушка: в реальности SAP RFC или OData."""
    df = pd.read_csv(path)
    print(f"Извлечено {len(df)} строк из {table}")
    return df

def extract_customers(path): return extract_from_csv(path, 'KNA1')
def extract_materials(path): return extract_from_csv(path, 'MARA')
def extract_orders(path): return extract_from_csv(path, 'VBAK')
