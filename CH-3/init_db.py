import sqlite3
# we need to learn pi mysql or psycopg2



conn = sqlite3.connect("SalesDB/sales.db") # here i just create a folder as salesdb and a file is automatically created as sales.db

print("Database created successfully") # here now the database is created but the database is empty so we need to create tables in it

cursor =conn.cursor()

# now we need to create tables in it

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT NOT NULL,
product_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
price REAL NOT NULL,
total REAL NOT NULL
)
""")


cursor.execute("""
INSERT INTO orders (customer_name, product_name, quantity, price, total) VALUES
("John Doe", "Laptop", 1, 1000.00, 1000.00),
("Jane Smith", "Smartphone", 2, 500.00, 1000.00),
("Bob Johnson", "Tablet", 3, 200.00, 600.00)
""")

conn.commit()
conn.close()
# we have the content manager also to do same things 
# what is benefit of using content manager  all the things will be done within this context is called context manager
# with cursor as cursor:
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     customer_name TEXT NOT NULL,
#     product_name TEXT NOT NULL,
#     quantity INTEGER NOT NULL,
#     price REAL NOT NULL,
#     total REAL NOT NULL
#     )
#     """) in this when write outside (""" inside """) if we write (""" inside """) it will give execution only  

