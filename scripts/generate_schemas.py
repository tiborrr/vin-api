
import psycopg


def map_type(pg_type):
    if pg_type in ['integer', 'smallint', 'bigint']:
        return 'int'
    elif pg_type in ['character varying', 'text', 'character', 'uuid', 'json', 'jsonb']:
        return 'str'
    elif pg_type in ['boolean']:
        return 'bool'
    elif pg_type in ['numeric', 'real', 'double precision']:
        return 'float'
    elif pg_type in ['date', 'timestamp without time zone', 'timestamp with time zone']:
        return 'datetime'
    else:
        return 'Any'

conn = psycopg.connect("postgresql://vpic:vpic_password@127.0.0.1:5433/vpic_db")
cur = conn.cursor()

cur.execute("""
    SELECT table_name, column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_schema = 'vpic'
    ORDER BY table_name, ordinal_position;
""")

tables = {}
for table_name, column_name, data_type, is_nullable in cur.fetchall():
    if table_name not in tables:
        tables[table_name] = []
    tables[table_name].append((column_name, data_type, is_nullable))

print("from pydantic import BaseModel, ConfigDict")
print("from typing import Optional, Any")
print("from datetime import datetime")
print("")

for table_name, columns in tables.items():
    class_name = ''.join(word.capitalize() for word in table_name.split('_'))
    print(f"class {class_name}(BaseModel):")
    print("    model_config = ConfigDict(from_attributes=True)")
    for col_name, dt, is_null in columns:
        py_type = map_type(dt)
        if is_null == 'YES':
            print(f"    {col_name}: Optional[{py_type}] = None")
        else:
            print(f"    {col_name}: {py_type}")
    print("")
