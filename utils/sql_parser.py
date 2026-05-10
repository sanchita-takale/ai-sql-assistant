import re

def extract_tables_and_db(sql_query):

    # Find tables after FROM / JOIN
    tables = re.findall(r'from\s+([a-zA-Z0-9_]+)|join\s+([a-zA-Z0-9_]+)', sql_query, re.IGNORECASE)

    table_list = []

    for t in tables:
        table_list.extend([x for x in t if x])

    return list(set(table_list))