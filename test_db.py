from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/ai_sql_project"
)

with engine.connect() as conn:
    print("Connected successfully!")