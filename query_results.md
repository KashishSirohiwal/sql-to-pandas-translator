# SQL to Pandas Translator Test Results

### SQL Query
```sql
SELECT * FROM sales LIMIT 5
```
**Expected:** First 5 rows of sales data

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi   |           101 |
|          2 | 2023-01-05 | Soap      | Toiletries |       40 | Delhi   |           102 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi   |           105 |

---

### SQL Query
```sql
SELECT product, amount FROM sales
```
**Expected:** Only product and amount columns

**Output:**

| product   |   amount |
|:----------|---------:|
| Shampoo   |      250 |
| Soap      |       40 |
| T-shirt   |      799 |
| Jeans     |     1599 |
| Perfume   |     1200 |
| Notebook  |       60 |
| Pen       |       15 |
| T-shirt   |      699 |
| Shampoo   |      300 |
| Perfume   |     1100 |

---

### SQL Query
```sql
SELECT product, amount FROM sales WHERE amount > 500
```
**Expected:** Products costing more than 500

**Output:**

| product   |   amount |
|:----------|---------:|
| T-shirt   |      799 |
| Jeans     |     1599 |
| Perfume   |     1200 |
| T-shirt   |      699 |
| Perfume   |     1100 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE city == 'Delhi'
```
**Expected:** All orders from Delhi

**Output:**

|   order_id | date       | product   | category   |   amount | city   |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:-------|--------------:|
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi  |           101 |
|          2 | 2023-01-05 | Soap      | Toiletries |       40 | Delhi  |           102 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi  |           105 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi  |           108 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE category == 'Clothing'
```
**Expected:** All clothing category orders

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi   |           108 |

---

### SQL Query
```sql
SELECT * FROM sales ORDER BY amount DESC
```
**Expected:** All rows sorted by amount in descending order

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi   |           105 |
|         10 | 2023-04-12 | Perfume   | Toiletries |     1100 | Gurgaon |           110 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi   |           108 |
|          9 | 2023-04-08 | Shampoo   | Toiletries |      300 | Noida   |           109 |
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi   |           101 |
|          6 | 2023-03-12 | Notebook  | Stationery |       60 | Noida   |           106 |
|          2 | 2023-01-05 | Soap      | Toiletries |       40 | Delhi   |           102 |
|          7 | 2023-03-20 | Pen       | Stationery |       15 | Gurgaon |           107 |

---

### SQL Query
```sql
SELECT product, amount FROM sales WHERE amount > 500 ORDER BY amount ASC
```
**Expected:** Products > 500 sorted in ascending order

**Output:**

| product   |   amount |
|:----------|---------:|
| T-shirt   |      699 |
| T-shirt   |      799 |
| Perfume   |     1100 |
| Perfume   |     1200 |
| Jeans     |     1599 |

---

### SQL Query
```sql
SELECT category, SUM(amount) FROM sales GROUP BY category
```
**Expected:** Total sales amount per category

**Output:**

| category   |   SUM(amount) |
|:-----------|--------------:|
| Clothing   |          3097 |
| Stationery |            75 |
| Toiletries |          2890 |

---

### SQL Query
```sql
SELECT city, COUNT(order_id) FROM sales GROUP BY city HAVING COUNT(order_id) > 2
```
**Expected:** Cities with more than 2 orders

**Output:**

| city    |   COUNT(order_id) |
|:--------|------------------:|
| Delhi   |                 4 |
| Gurgaon |                 3 |
| Noida   |                 3 |

---

### SQL Query
```sql
SELECT DISTINCT city FROM sales
```
**Expected:** Unique cities in dataset

**Output:**

| city    |
|:--------|
| Delhi   |
| Gurgaon |
| Noida   |

---

### SQL Query
```sql
SELECT DISTINCT category FROM sales WHERE amount > 1000
```
**Expected:** Unique categories where sales amount > 1000

**Output:**

| category   |
|:-----------|
| Clothing   |
| Toiletries |

---

### SQL Query
```sql
SELECT * FROM sales LIMIT 5 ORDER BY amount DESC
```
**Expected:** Top 5 rows ordered by amount descending

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi   |           105 |
|         10 | 2023-04-12 | Perfume   | Toiletries |     1100 | Gurgaon |           110 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi   |           108 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE amount > 100 LIMIT 3
```
**Expected:** First 3 rows where amount > 100

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi   |           101 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |

---

### SQL Query
```sql
SELECT product, amount FROM sales WHERE city == 'Delhi' AND amount > 500
```
**Expected:** Delhi orders where amount > 500

**Output:**

| product   |   amount |
|:----------|---------:|
| Perfume   |     1200 |
| T-shirt   |      699 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE category == 'Clothing' OR amount < 100 ORDER BY amount ASC
```
**Expected:** Orders where category=Clothing or amount<100

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          7 | 2023-03-20 | Pen       | Stationery |       15 | Gurgaon |           107 |
|          2 | 2023-01-05 | Soap      | Toiletries |       40 | Delhi   |           102 |
|          6 | 2023-03-12 | Notebook  | Stationery |       60 | Noida   |           106 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi   |           108 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE amount BETWEEN 100 AND 1000
```
**Expected:** Orders with amount between 100 and 1000

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi   |           101 |
|          3 | 2023-01-10 | T-shirt   | Clothing   |      799 | Gurgaon |           103 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi   |           108 |
|          9 | 2023-04-08 | Shampoo   | Toiletries |      300 | Noida   |           109 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE date BETWEEN '2023-02-01' AND '2023-03-31'
```
**Expected:** Orders placed between Feb 1 and Mar 31, 2023

**Output:**

|   order_id | date       | product   | category   |   amount | city    |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:--------|--------------:|
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida   |           104 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi   |           105 |
|          6 | 2023-03-12 | Notebook  | Stationery |       60 | Noida   |           106 |
|          7 | 2023-03-20 | Pen       | Stationery |       15 | Gurgaon |           107 |

---

### SQL Query
```sql
SELECT * FROM sales WHERE city IN ('Delhi', 'Noida')
```
**Expected:** Orders from Delhi or Noida

**Output:**

|   order_id | date       | product   | category   |   amount | city   |   customer_id |
|-----------:|:-----------|:----------|:-----------|---------:|:-------|--------------:|
|          1 | 2023-01-03 | Shampoo   | Toiletries |      250 | Delhi  |           101 |
|          2 | 2023-01-05 | Soap      | Toiletries |       40 | Delhi  |           102 |
|          4 | 2023-02-01 | Jeans     | Clothing   |     1599 | Noida  |           104 |
|          5 | 2023-02-10 | Perfume   | Toiletries |     1200 | Delhi  |           105 |
|          6 | 2023-03-12 | Notebook  | Stationery |       60 | Noida  |           106 |
|          8 | 2023-04-05 | T-shirt   | Clothing   |      699 | Delhi  |           108 |
|          9 | 2023-04-08 | Shampoo   | Toiletries |      300 | Noida  |           109 |

---

### SQL Query
```sql
SELECT product, amount FROM sales WHERE category IN ('Clothing', 'Stationery')
```
**Expected:** Products in Clothing or Stationery categories

**Output:**

| product   |   amount |
|:----------|---------:|
| T-shirt   |      799 |
| Jeans     |     1599 |
| Notebook  |       60 |
| Pen       |       15 |
| T-shirt   |      699 |

---

