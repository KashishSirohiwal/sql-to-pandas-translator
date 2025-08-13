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
            condition = str(token).lstrip("WHERE").strip()

            # Split into parts: column, operator, value
            parts = condition.split()
            if len(parts) == 3 and parts[2].isalpha():
                parts[2] = f'"{parts[2]}"'
                condition = " ".join(parts)

            return condition
    return None

def extract_order_by(parsed):
    tokens = list(parsed.tokens)
    for i, token in enumerate(tokens):
        if token.ttype is Keyword and token.value.upper() == "ORDER BY":
            # Find the next non-whitespace token
            j = i + 1
            while j < len(tokens) and tokens[j].is_whitespace:
                j += 1

            if j >= len(tokens):
                return None  # No column found after ORDER BY

            next_token = tokens[j]            
            parts1 = str(next_token).split()
            
            column_name = parts1[0]
            ascending_boolean = True # Default to ASC
            if len(parts1) > 1 and parts1[1].upper() == "DESC":
                ascending_boolean = False
            return (column_name, ascending_boolean)
    return None

def sql_to_pandas_select(query):
    parsed = sqlparse.parse(query)[0]
    columns = extract_columns(parsed)
    where_clause = extract_where(parsed)
    order_by_info = extract_order_by(parsed)

    # Start with base dataframe
    if not columns or columns == ['*']:
        result_df = df.copy()
    else:
        result_df = df[columns]
    
    # Apply WHERE if present
    if where_clause:
        result_df = result_df.query(where_clause)

    # Apply ORDER BY if present
    if order_by_info:
        column_name, ascending_boolean = order_by_info
        result_df = result_df.sort_values(by=column_name, ascending=ascending_boolean)

    return result_df

if __name__ == "__main__":
    # Test queries
    print(sql_to_pandas_select("SELECT * FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales WHERE amount > 500"))
    print(sql_to_pandas_select("SELECT * FROM sales WHERE city == Delhi"))
    print(sql_to_pandas_select("SELECT * FROM sales WHERE category == Clothing"))
    print(sql_to_pandas_select("SELECT * FROM sales ORDER BY amount DESC"))
    print(sql_to_pandas_select("SELECT product, amount FROM sales WHERE amount > 500 ORDER BY amount ASC"))