import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bbs"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM addr_divisions")

myresult = mycursor.fetchall()

for row in myresult:
    state = "INSERT INTO `state` (`created`, `updated`, `uuid`, `is_deleted`, `is_active`, `name`, `code`, `other`, `bbs_code`, `country_id`) VALUES ("
    state += "now(), now(), UUID(), 0, 1,'" + str(row[6]).capitalize() + "', '', , '', " + str(row[9]) + ",17);"
    # print(str(row[0]) + " " + str(row[6]).capitalize())
    print(state)