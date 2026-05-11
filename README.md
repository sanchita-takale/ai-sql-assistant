# 🚀 AI SQL Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![SQL](https://img.shields.io/badge/SQL-MySQL%20%7C%20PostgreSQL-orange?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-success?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge)

### 💡 Ask Questions in Plain English → Get SQL Queries, Results & Insights Instantly

An AI-powered SQL Assistant that enables users to interact with databases using natural language.  
Generate SQL queries, execute them on databases, visualize results, and receive AI-generated business insights — all from a simple Streamlit interface.

</div>

---

# 📌 Project Overview

AI SQL Assistant is designed to simplify database interaction for:

- 👨‍🎓 SQL Beginners
- 📊 Data Analysts
- 👨‍💻 Developers
- 📈 Business Users

Instead of writing complex SQL manually, users can ask questions like:

> "Top 5 customers by revenue"

The assistant automatically:

✅ Generates SQL  
✅ Executes query  
✅ Displays results  
✅ Creates visualizations  
✅ Generates AI business insights

---

# ✨ Features

## 🧠 AI-Powered SQL Generation
Convert natural language questions into SQL queries using LLMs.

## 🗄️ Database Integration
Supports:
- MySQL
- PostgreSQL

## 📊 Automatic Visualization
Generate charts automatically from query results.

## 💬 AI Business Insights
Get intelligent explanations and insights from query outputs.

## 🔒 Secure Environment Handling
API keys and database credentials stored securely using `.env`.

## 🎨 Beginner-Friendly UI
Simple and interactive Streamlit interface.

---

# 🏗️ Architecture / Workflow

```text
User Question
      ↓
LLM (Gemini/OpenAI/Groq)
      ↓
SQL Query Generation
      ↓
SQL Safety Validation
      ↓
Database Execution
      ↓
Query Results
      ↓
Visualization + AI Insights