# backend/utils/check_tables.py

from backend.config.database import engine
from sqlalchemy import inspect

inspector = inspect(engine)

tables = inspector.get_table_names()

print("\nTables Found:\n")

for table in tables:
    print(table)