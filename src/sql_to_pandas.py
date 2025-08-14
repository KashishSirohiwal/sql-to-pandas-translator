import pandas as pd
import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where, Function
from sqlparse.tokens import Keyword, DML

# Load your dataset
df = pd.read_csv("data/sales.csv")

def extract_columns(parsed):
    columns = []
    select_seen = False
    for tok in parsed.tokens:
        if tok.ttype is DML and tok.value.upper() == "SELECT":
            select_seen = True
        elif select_seen:
            if isinstance(tok, IdentifierList):
                for ident in tok.get_identifiers():
                    if isinstance(ident, Function):
                        columns.append(str(ident))  # keep functions like SUM(amount)
                    else:
                        columns.append(ident.get_name())
                break
            elif isinstance(tok, Identifier):
                columns.append(tok.get_name())
                break
            elif isinstance(tok, Function):
                columns.append(str(tok))
                break
            elif tok.ttype is Keyword and tok.value.upper() == "FROM":
                break
    return columns

def extract_where(parsed):
    for token in parsed.tokens:
        if isinstance(token, Where):
            condition = str(token).lstrip("WHERE").strip()
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
            j = i + 1
            while j < len(tokens) and tokens[j].is_whitespace:
                j += 1
            if j >= len(tokens):
                return None
            next_token = tokens[j]
            parts1 = str(next_token).split()
            column_name = parts1[0]
            ascending_boolean = True
            if len(parts1) > 1 and parts1[1].upper() == "DESC":
                ascending_boolean = False
            return (column_name, ascending_boolean)
    return None

def extract_group_by(parsed):
    group_by_column = None
    tokens = list(parsed.tokens)

    # Find GROUP BY column
    for i, token in enumerate(tokens):
        if token.ttype is Keyword and token.value.upper() == "GROUP BY":
            j = i + 1
            while j < len(tokens) and tokens[j].is_whitespace:
                j += 1
            if j < len(tokens):
                if isinstance(tokens[j], Identifier):
                    group_by_column = tokens[j].get_name()
                else:
                    group_by_column = str(tokens[j]).strip()
            break

    # Detect aggregate function in SELECT
    agg_func = None
    agg_column = None
    for tok in parsed.tokens:
        if isinstance(tok, IdentifierList):
            for ident in tok.get_identifiers():
                if isinstance(ident, Function):
                    agg_func = ident.get_name()
                    params = ident.get_parameters()
                    if params:
                        agg_column = params[0].get_name()
        elif isinstance(tok, Function):
            agg_func = tok.get_name()
            params = tok.get_parameters()
            if params:
                agg_column = params[0].get_name()
    return (group_by_column, agg_column, agg_func)

def sql_to_pandas_select(query):
    parsed = sqlparse.parse(query)[0]
    columns = extract_columns(parsed)
    where_clause = extract_where(parsed)
    order_by_info = extract_order_by(parsed)
    group_by_info = extract_group_by(parsed)

    result_df = df.copy()

    # WHERE
    if where_clause:
        result_df = result_df.query(where_clause)

    # GROUP BY
    if group_by_info:
        group_by_column, agg_column, agg_func = group_by_info
        agg_map = {
            'SUM': 'sum',
            'COUNT': 'count',
            'AVG': 'mean',
            'MEAN': 'mean',
            'MAX': 'max',
            'MIN': 'min'
        }
        if group_by_column and agg_column and agg_func and agg_func.upper() in agg_map:
            result_df = (
                result_df
                .groupby(group_by_column, as_index=False)[agg_column]
                .agg(agg_map[agg_func.upper()])
            )
            # Rename for SQL-like column name
            result_df.rename(columns={agg_column: f"{agg_func.upper()}({agg_column})"}, inplace=True)

    # SELECT columns
    if columns and columns != ['*']:
        keep = [c for c in columns if c in result_df.columns]
        if keep:
            result_df = result_df[keep]

    # ORDER BY
    if order_by_info:
        column_name, ascending_boolean = order_by_info
        if column_name in result_df.columns:
            result_df = result_df.sort_values(by=column_name, ascending=ascending_boolean)

    return result_df

if __name__ == "__main__":
    print(sql_to_pandas_select("SELECT * FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales").head())
    print(sql_to_pandas_select("SELECT product, amount FROM sales WHERE amount > 500"))
    print(sql_to_pandas_select("SELECT * FROM sales WHERE city == 'Delhi'"))
    print(sql_to_pandas_select("SELECT * FROM sales WHERE category == 'Clothing'"))
    print(sql_to_pandas_select("SELECT * FROM sales ORDER BY amount DESC"))
    print(sql_to_pandas_select("SELECT product, amount FROM sales WHERE amount > 500 ORDER BY amount ASC"))
    print(sql_to_pandas_select("SELECT category, SUM(amount) FROM sales GROUP BY category"))
    print(sql_to_pandas_select("SELECT city, COUNT(order_id) FROM sales GROUP BY city ORDER BY COUNT(order_id) DESC"))
    print(sql_to_pandas_select("SELECT category, AVG(amount) FROM sales WHERE city == 'Delhi' GROUP BY category"))