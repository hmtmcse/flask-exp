import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="billing"
)

db_cursor = mydb.cursor()


# INSERT QUERY
sql = "INSERT INTO amount (name, amount) VALUES (%s, %s)"
val = ("Apple", 20)
db_cursor.execute(sql, val)
mydb.commit()
print(db_cursor.rowcount, "record inserted.")

# SELECT QUERY
db_cursor.execute("SELECT * FROM amount")
select_result = db_cursor.fetchall()

for row in select_result:
  print(row)

# Update
sql = "UPDATE amount SET name = 'ABC' WHERE amount = 20"
db_cursor.execute(sql)
mydb.commit()
print(db_cursor.rowcount, "record(s) affected")

# DELETE
sql = "DELETE FROM amount WHERE amount = 20"
db_cursor.execute(sql)
mydb.commit()
print(db_cursor.rowcount, "record(s) deleted")



