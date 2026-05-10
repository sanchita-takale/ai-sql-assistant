from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/ai_sql_project"
)

def run_query(query):

    with engine.connect() as conn:

        result = conn.execute(text(query))

        rows = result.fetchall()

        columns = result.keys()

        df = pd.DataFrame(rows, columns=columns)

        return df