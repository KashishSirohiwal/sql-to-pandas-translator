import pandas as pd
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML

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

def sql_to_pandas_select(query):
    parsed = sqlparse.parse(query)[0]
    columns = extract_columns(parsed)
    if not columns or columns == ['*']:
        return df
    else:
        return df[columns]

if __name__ == "__main__":
    # Test queries
    print(sql_to_pandas_select("SELECT * FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales").head())