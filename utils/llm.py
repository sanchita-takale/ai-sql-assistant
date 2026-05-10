
#------------------------
#This code is for Gemini API
#------------------------

# from google import genai
# from dotenv import load_dotenv
# import os
# import time

# load_dotenv()

# client = genai.Client(
#     # api_key=os.getenv("GEMINI_API_KEY")
    
# )

# MODELS = [
#     "gemini-2.0-flash",
#     "gemini-2.0-flash-lite"
# ]

# def clean_sql(sql):

#     sql = sql.replace("```sql", "")
#     sql = sql.replace("```mysql", "")
#     sql = sql.replace("```", "")

#     return sql.strip()


# def generate_sql(question):

#     prompt = f"""
#     Convert the following business question into SQL.

#     Question:
#     {question}

#     Return ONLY SQL query.
#     """

#     last_error = None

#     for model_name in MODELS:

#         try:

#             response = client.models.generate_content(
#                 model=model_name,
#                 contents=prompt
#             )

#             return clean_sql(response.text)

#         except Exception as e:

#             print(f"Model failed: {model_name}")
#             print(e)

#             last_error = e

#             time.sleep(2)

#     raise Exception(
#         f"All Gemini models failed.\n{last_error}"
#     )


#------------------------
#This code is for Gorq API
#------------------------

from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_sql(text):

    # Remove markdown SQL blocks
    text = re.sub(r"```sql", "", text)
    text = re.sub(r"```", "", text)

    # Keep only SELECT query
    match = re.search(
        r"(SELECT.*?;)",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return text.strip()

def generate_sql(question):

    prompt = f"""
    You are an expert SQL generator.

    Database tables:

    customers(
        customer_id
    )

    orders(
        order_id,
        customer_id,
        order_date,
        total_amount
    )

    Convert the following question into MySQL query.

    Return ONLY SQL query.

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    raw_output = response.choices[0].message.content

    sql_query = extract_sql(raw_output)

    return sql_query