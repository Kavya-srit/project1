import mysql.connector
mydb=mysql.connector.connect(host='localhost',username='root',password='KavyaSri@1613',database='Inventory_Management')

# Create cursor object
mycursor = mydb.cursor()

# Create manufacture table
T1='CREATE TABLE manufacture (id INTEGER AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(100), items_required INTEGER, defective_items INTEGER)'
mycursor.execute(T1)

# Create goods table
T2='CREATE TABLE goods (id INTEGER AUTO_INCREMENT PRIMARY KEY, goods_name VARCHAR(100), manufactured_date DATE)'
mycursor.execute(T2)

# Create purchase table
T3='CREATE TABLE purchase (id INTEGER AUTO_INCREMENT PRIMARY KEY, store_name VARCHAR(100), purchase_amount FLOAT)'
mycursor.execute(T3)

# Create sale table
T4='CREATE TABLE sales (id INTEGER AUTO_INCREMENT PRIMARY KEY, store_name VARCHAR(100), sale_date DATE, profit_margin FLOAT, goods_id INTEGER)'
mycursor.execute(T4)

# Insert data into manufacture table
Q1 = "INSERT INTO manufacture (product_name, items_required, defective_items) VALUES (%s, %s, %s)"
val1 = [
  ('Toy Car', 500, 5),
  ('Red Toy', 200, 2),
  ('Wooden Chair', 100, 1),
  ('Wooden Table', 50, 0)
]
mycursor.executemany(Q1, val1)

mycursor.execute("select * from manufacture")
for row in mycursor:
  print(row)

# Insert data into goods table
Q2 = "INSERT INTO goods (goods_name, manufactured_date) VALUES (%s, %s)"
val2 = [
  ('Toy Car', '2023-05-01'),
  ('Red Toy', '2023-04-28'),
  ('Wooden Chair', '2023-04-29'),
  ('Wooden Table', '2023-04-30')
]
mycursor.executemany(Q2, val2)

# Insert data into purchase table

Q3 = "INSERT INTO purchase (store_name, purchase_amount) VALUES (%s, %s)"
val3 = [
  ('ORay', 500.0),
  ('MyKids', 200.0),
  ('MyCare', 1000.0),
  ('Amazon', 5000.0)
]
mycursor.executemany(Q3, val3)

# Insert data into sale table
Q4 = "INSERT INTO sales (store_name, sale_date, profit_margin, goods_id) VALUES (%s, %s, %s, %s)"
val4 = [
  ('MyCare', '2023-05-01', 100.0, 4),
  ('ORay', '2023-04-30', 50.0, 1),
  ('MyKids', '2023-05-01', 150.0, 2),
  ('Amazon', '2023-05-02', 250.0, 3)
]
mycursor.executemany(Q4, val4)

# Delete defective item from goods table
Q5 = "DELETE FROM goods WHERE goods_name = 'Red Toy' AND manufactured_date = '2023-04-28'"
mycursor.execute(Q5)

# Update manufacture details of red-colored toys purchased by MyKids store
Q6 = "UPDATE manufacture SET items_required = 250 WHERE product_name = 'Red Toy'"
mycursor.execute(Q6)

# Display wooden chairs manufactured before 1st May 2023
Q7 = "SELECT * FROM goods WHERE goods_name = 'Wooden Chair' AND manufactured_date < '2023-05-01'" 
mycursor.execute(Q7)
result = mycursor.fetchall()
for row in result:
  print(row)

# Display profit margin of wooden table sold by SS Export to MyCare store
Q8 = "SELECT profit_margin FROM sale JOIN goods ON sale.goods_id = goods.id WHERE goods.goods_name = 'Wooden Table' AND sale.store_name = 'MyCare'"
mycursor.execute(Q8)
result = mycursor.fetchone()
print(result)

# Commit changes to database
mydb.commit()

# Close database connection
mydb.close()


