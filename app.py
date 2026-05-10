import streamlit as st
import pandas as pd

from utils.llm import generate_sql
from utils.db import run_query
from utils.security import is_safe_query
from utils.insights import generate_insights
from utils.sql_parser import extract_tables_and_db

st.set_page_config(
    page_title="AI SQL Assistant",
    layout="wide"
)

st.title("AI SQL Assistant")
st.subheader("📊 Connected Data Source")

st.info("""
🗄️ Database: ecommerce_db  
📁 Tables:
- customers  
- orders  
- products  
- payments
""")

st.write(
    "Ask business questions in plain English"
)

user_question = st.text_input(
    "Enter your business question:"
)

generate = st.button("Generate Query")

if user_question and (
    generate or st.session_state.get("last_question") != user_question
):

    st.session_state["last_question"] = user_question

    try:

        # Generate SQL
        sql_query = generate_sql(user_question)

        st.subheader("Generated SQL")

        st.code(sql_query, language="sql")

        st.subheader("Query Metadata")

        tables = extract_tables_and_db(sql_query)

        st.info(
            f"📊 Tables used: {', '.join(tables) if tables else 'Not detected'}"
        )

        # Validate SQL
        if not is_safe_query(sql_query):

            st.error("Unsafe query blocked")

        else:

            # Run query
            df = run_query(sql_query)

            st.subheader("Query Result")

            st.dataframe(df)

            # FORCE numeric conversion
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # Download CSV
            csv = df.to_csv(index=False)

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="query_result.csv",
                mime="text/csv"
            )

            # Auto chart
            st.subheader("Visualization")

            try:
                df = df.copy()

                # -----------------------------
                # STEP 1: CLEAN NUMBERS SAFELY
                # -----------------------------
                import re

                def clean(x):
                    if isinstance(x, str):
                        x = re.sub(r'[^0-9.\-]', '', x)
                    try:
                        return float(x)
                    except:
                        return None

                for col in df.columns:
                    df[col] = df[col].apply(clean)

                # -----------------------------
                # STEP 2: IDENTIFY COLUMNS
                # -----------------------------
                numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                text_cols = df.select_dtypes(exclude=['number']).columns.tolist()

                if not numeric_cols:
                    st.warning("No numeric data to plot")

                else:
                    y = numeric_cols[-1]   # IMPORTANT: use last metric (not first)

                    # -----------------------------
                    # CASE 1: TIME SERIES (REAL TREND)
                    # -----------------------------
                    if 'year' in df.columns and 'month' in df.columns:

                        df = df.dropna(subset=['year', 'month'])

                        df['year'] = df['year'].astype(int)
                        df['month'] = df['month'].astype(int)

                        df = df.sort_values(['year', 'month'])

                        df['date'] = df['year'].astype(str) + "-" + df['month'].astype(str)

                        chart = df.groupby('date')[y].mean()   # 🔥 mean not sum

                        st.line_chart(chart)

                    # -----------------------------
                    # CASE 2: RANKING (Top N)
                    # -----------------------------
                    elif len(text_cols) > 0:

                        x = text_cols[0]

                        df = df.dropna(subset=[x])

                        chart = df.groupby(x)[y].sum()

                        st.bar_chart(chart)

                    # -----------------------------
                    # CASE 3: FALLBACK (NO FLAT LINE)
                    # -----------------------------
                    else:

                        chart = df[y]

                        st.line_chart(chart)

            except Exception as e:
                st.error(f"Visualization error: {e}")

            # AI Insights
            st.subheader("AI Business Insights")

            insights = generate_insights(
                user_question,
                df.head(10).to_string()
            )

            st.write(insights)

            st.success(
                "Query executed successfully"
            )

    except Exception as e:

        if "429" in str(e):

            st.error(
                "Daily Gemini API limit exceeded. Try again later."
            )

        elif "503" in str(e):

            st.error(
                "Gemini servers are busy right now. Please retry."
            )

        else:

            st.error(f"Error: {str(e)}")