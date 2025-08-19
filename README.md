# SQL → Pandas Translator

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](https://github.com/KashishSirohiwal/sql-to-pandas-translator/issues)

> A lightweight project that **translates SQL queries into Pandas DataFrame operations**.  
> Designed as a learning tool to bridge the gap between SQL and Python for data analysis.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Quickstart](#quickstart)
- [Supported SQL Syntax](#supported-sql-syntax)
- [Sample Outputs](#sample-outputs)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## Features
- Run SQL-style queries directly on Pandas DataFrames  
- Supports major SQL clauses:  
  - `SELECT`, `WHERE`, `AND` / `OR`  
  - `BETWEEN` (numeric + date ranges)  
  - `IN (...)`  
  - `ORDER BY col ASC|DESC`  
  - `DISTINCT`  
  - `GROUP BY` + aggregates (`SUM`, `COUNT`, `AVG`, `MIN`, `MAX`)  
  - `HAVING`  
  - `LIMIT`  
- Auto-generates Markdown report (`query_results.md`) with query outputs  

---

## Project Structure
```
.
├─ data/
│ └─ sales.csv           # sample dataset
├─ notebooks/
│ └─ quick_refresher.py  # helper / scratchpad
├─ src/
│ └─ sql_to_pandas.py    # SQL → Pandas translator logic
├─ test_queries.py       # runs all queries + saves outputs
├─ query_results.md      # results of all queries in table form
├─ requirements.txt      # dependencies
└─ README.md             # documentation
```
---
## Quickstart

### 1. Clone & Setup

git clone https://github.com/KashishSirohiwal/sql-to-pandas-translator.git<br>
cd sql-to-pandas-translator

```# create environment ```<br>
python -m venv .venv<br>
.\.venv\Scripts\activate     ```# Windows```<br>
```# or source .venv/bin/activate (Linux/Mac)```<br>
<br>
```# install dependencies```<br>
pip install -r requirements.txt
<br>

### 2. Run Queries

python test_queries.py<br>
```# This will execute all sample queries and save their outputs in query_results.md.```<br>

### 3. Use in Code

from src.sql_to_pandas import sql_to_pandas_select<br>
<br>
df = sql_to_pandas_select(<br>
    "SELECT category, SUM(amount) FROM sales GROUP BY category HAVING SUM(amount) > 2000"<br>
)<br>
print(df)<br>

---
