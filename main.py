from utils.llm import generate_sql
from utils.db import run_query

question = input("Ask a business question: ")

# Generate SQL from AI
sql_query = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql_query)

# Run query in MySQL
result = run_query(sql_query)

print("\nQuery Result:\n")

for row in result:

    clean_row = []

    for value in row:

        if hasattr(value, "quantize"):
            clean_row.append(float(value))
        else:
            clean_row.append(value)

    print(tuple(clean_row))