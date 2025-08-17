import pandas as pd
from src.sql_to_pandas import sql_to_pandas_select

OUTPUT_FILE = "query_results.md"

def run_query(query, expected=None):
    print("🔹 SQL Query:", query)
    if expected:
        print("✅ Expected:", expected)

    try:
        result = sql_to_pandas_select(query)

        # Print in console
        print("📊 Actual Output:\n", result, "\n")

        # Save to markdown
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"### SQL Query\n```sql\n{query}\n```\n")
            if expected:
                f.write(f"**Expected:** {expected}\n\n")
            f.write("**Output:**\n\n")
            f.write(result.to_markdown(index=False))
            f.write("\n\n---\n\n")

    except Exception as e:
        print("❌ Error:", e, "\n")
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"### SQL Query\n```sql\n{query}\n```\n")
            f.write(f"❌ Error: {e}\n\n---\n\n")

if __name__ == "__main__":
    # Clear old output file
    open(OUTPUT_FILE, "w", encoding="utf-8").write("# SQL to Pandas Translator Test Results\n\n")

    # Basic Queries
    run_query("SELECT * FROM sales LIMIT 5", "First 5 rows of sales data")
    run_query("SELECT product, amount FROM sales", "Only product and amount columns")
    run_query("SELECT product, amount FROM sales WHERE amount > 500", "Products costing more than 500")
    run_query("SELECT * FROM sales WHERE city == 'Delhi'", "All orders from Delhi")
    run_query("SELECT * FROM sales WHERE category == 'Clothing'", "All clothing category orders")

    # ORDER BY
    run_query("SELECT * FROM sales ORDER BY amount DESC", "All rows sorted by amount in descending order")
    run_query("SELECT product, amount FROM sales WHERE amount > 500 ORDER BY amount ASC", "Products > 500 sorted in ascending order")

    # GROUP BY + HAVING
    run_query("SELECT category, SUM(amount) FROM sales GROUP BY category", "Total sales amount per category")
    run_query("SELECT city, COUNT(order_id) FROM sales GROUP BY city HAVING COUNT(order_id) > 2", "Cities with more than 2 orders")

    # DISTINCT
    run_query("SELECT DISTINCT city FROM sales", "Unique cities in dataset")
    run_query("SELECT DISTINCT category FROM sales WHERE amount > 1000", "Unique categories where sales amount > 1000")

    # LIMIT
    run_query("SELECT * FROM sales LIMIT 5 ORDER BY amount DESC", "Top 5 rows ordered by amount descending")
    run_query("SELECT * FROM sales WHERE amount > 100 LIMIT 3", "First 3 rows where amount > 100")

    # AND / OR
    run_query("SELECT product, amount FROM sales WHERE city == 'Delhi' AND amount > 500", "Delhi orders where amount > 500")
    run_query("SELECT * FROM sales WHERE category == 'Clothing' OR amount < 100 ORDER BY amount ASC", "Orders where category=Clothing or amount<100")

    # BETWEEN
    run_query("SELECT * FROM sales WHERE amount BETWEEN 100 AND 1000", "Orders with amount between 100 and 1000")
    run_query("SELECT * FROM sales WHERE date BETWEEN '2023-02-01' AND '2023-03-31'", "Orders placed between Feb 1 and Mar 31, 2023")

    # IN
    run_query("SELECT * FROM sales WHERE city IN ('Delhi', 'Noida')", "Orders from Delhi or Noida")
    run_query("SELECT product, amount FROM sales WHERE category IN ('Clothing', 'Stationery')", "Products in Clothing or Stationery categories")