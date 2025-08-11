import pandas as pd
df = pd.read_csv('data/sales.csv', parse_dates=['date'])

print("=== SELECT columns ===")
print(df[['product','amount']].head(), "\n")

print("=== WHERE filter amount > 700 ===")
print(df[df['amount'] > 700], "\n")

print("=== GROUP BY category total sales ===")
print(df.groupby('category')['amount'].sum().reset_index(), "\n")