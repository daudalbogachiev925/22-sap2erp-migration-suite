# SAP → ERP миграция

Этапы:
1. Extract — выгрузка из SAP (RFC/OData/CSV)
2. Transform — маппинг полей, очистка, дедупликация
3. Load — upsert в целевую БД (Postgres)
4. Reconcile — сравнение количества и сумм

Маппинг в config/mapping.yaml:
- KNA1 → clients
- MARA → products
- VBAK → orders

Идемпотентность: ON CONFLICT DO UPDATE.
