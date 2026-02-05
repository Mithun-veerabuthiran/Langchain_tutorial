import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

# output : 
# (langchain-tutorial) PS C:\Users\acer\Desktop\Langchain_tutorial\CH-3> python .\demo.py
# (1, 'John Doe', 'Laptop', 1, 1000.0, 1000.0)
# (2, 'Jane Smith', 'Smartphone', 2, 500.0, 1000.0)
# (3, 'Bob Johnson', 'Tablet', 3, 200.0, 600.0)