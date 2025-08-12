import pandas as pd
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML
from sqlparse.sql import Where

# Load your dataset
df = pd.read_csv("data/sales.csv")

def extract_columns(parsed):
    columns = []
    select_seen = False
    for token in parsed.tokens:
        if token.ttype is DML and token.value.upper() == "SELECT":
            select_seen = True
        elif select_seen:
            if isinstance(token, IdentifierList):
                for identifier in token.get_identifiers():
                    columns.append(identifier.get_name())
                break
            elif isinstance(token, Identifier):
                columns.append(token.get_name())
                break
            elif token.ttype is Keyword and token.value.upper() == "FROM":
                break
    return columns

def extract_where(parsed):
    """
    Extracts WHERE condition from SQL query.
    """
    for token in parsed.tokens:
        if isinstance(token, Where):
            return str(token).lstrip("WHERE").strip()
            return condition
    return None

def sql_to_pandas_select(query):
    parsed = sqlparse.parse(query)[0]
    columns = extract_columns(parsed)
    where_clause = extract_where(parsed)

    if not columns or columns == ['*']:
        result_df = df.copy()
    else:
        result_df = df[columns]
    if where_clause:
        result_df = result_df.query(where_clause)

    return result_df

if __name__ == "__main__":
    # Test queries
    print(sql_to_pandas_select("SELECT * FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales WHERE amount > 500"))