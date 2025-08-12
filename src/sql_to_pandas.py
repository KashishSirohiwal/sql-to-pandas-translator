import pandas as pd
import sqlparse

# Load your dataset
df = pd.read_csv("data/sales.csv")

def sql_to_pandas_select(query):
    # Parse SQL
    parsed = sqlparse.parse(query)[0]
    tokens = [str(token).strip() for token in parsed.tokens if str(token).strip()]

    # Extract column names between SELECT and FROM
    if "SELECT" in tokens and "FROM" in tokens:
        select_index = tokens.index("SELECT")
        from_index = tokens.index("FROM")
        columns_str = tokens[select_index + 1]  # columns part
        columns = [col.strip() for col in columns_str.split(",")]

        # If selecting all columns
        if "*" in columns:
            return df
        else:
            return df[columns]
    else:
        raise ValueError("Invalid SQL query format.")

if __name__ == "__main__":
    # Test queries
    print(sql_to_pandas_select("SELECT * FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales").head())