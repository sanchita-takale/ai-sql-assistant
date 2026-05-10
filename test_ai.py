from utils.llm import generate_sql

question = "Top 5 customers by revenue"

sql_query = generate_sql(question)

print(sql_query)