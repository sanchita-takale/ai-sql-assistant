#------------------------
#This code is for Gemini API
#------------------------

# import time
# from google import genai

# client = genai.Client(
#     # api_key=os.getenv("GEMINI_API_KEY")    
# )

# MODELS = [
#     "gemini-2.0-flash",
#     "gemini-2.0-flash-lite"
# ]

# def generate_insights(question, data):

#     prompt = f"""
#     You are a business analyst.

#     Question:
#     {question}

#     Data:
#     {data}

#     Give short business insights in simple language.
#     """

#     for attempt in range(3):

#         try:

#             response = client.models.generate_content(
#                 model=model_name,
#                 contents=prompt
#             )

#             return response.text

#         except Exception as e:

#             print("Retrying insights...", e)

#             time.sleep(5)

#     return "Unable to generate AI insights right now."


#------------------------
#This code is for Gorq API
#------------------------

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_insights(question, data):

    try:

        prompt = f"""
        You are a business analyst.

        Question:
        {question}

        Query Result:
        {data}

        Give short business insights in simple English.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Insights generation failed: {str(e)}"