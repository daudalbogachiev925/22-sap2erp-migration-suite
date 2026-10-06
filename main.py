import sys, yaml
from sqlalchemy import create_engine
from extract.extract_sap import extract_customers, extract_materials, extract_orders
from transform.transform import transform
from load.load import load_all
from reconcile.reconcile import compare_counts, compare_sums

def main():
    engine = create_engine('postgresql://admin:admin@localhost/erp')

    print("=== Extract ===")
    raw = {}
    for name, path in [('customers','data/customers.csv'),
                       ('materials','data/materials.csv'),
                       ('orders','data/orders.csv')]:
        try:
            raw[name] = {'customers': extract_customers,
                         'materials': extract_materials,
                         'orders':    extract_orders}[name](path)
        except FileNotFoundError:
            print(f"Пропуск {name}: файл не найден")

    print("\n=== Transform ===")
    transformed = {k: transform(v, k) for k, v in raw.items()}
    for k, v in transformed.items():
        print(f"{k}: {len(v)} строк")

    print("\n=== Load ===")
    load_all(transformed, engine)

    print("\n=== Reconcile ===")
    if 'customers' in transformed:
        print("customers:", compare_counts(transformed['customers'], 'clients', engine))
    if 'orders' in transformed:
        print("orders sum:", compare_sums(transformed['orders'], 'orders', 'amount', engine))

if __name__ == '__main__':
    main()
