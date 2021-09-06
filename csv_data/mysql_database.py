import mysql.connector


class BDGeoLocation:
    mysql_database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bbs"
    )

    division_sql = ""
    division_index = 1

    upozzila_sql = ""
    upozzila_index = 1

    district_sql = ""
    district_index = 1

    def process_upozzila(self, district_id, district_db_id):
        mycursor = self.mysql_database.cursor()
        mycursor.execute("SELECT * FROM addr_upazilas WHERE district_id = " + district_db_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            self.upozzila_sql += "INSERT INTO `street` (`id`, `created`, `updated`, `uuid`, `is_deleted`, `is_active`, `name`, `code`, `other`, `bbs_code`, `city_id`) VALUES ("
            self.upozzila_sql += str(self.upozzila_index) + ", now(), now(), UUID(), 0, 1,'" + str(row[6]).capitalize() + "', '', '', " + str(row[10]) + "," + str(district_id) + ");\n"
            self.upozzila_index += 1

    def process_district(self, division_id, division_db_id):
        mycursor = self.mysql_database.cursor()
        mycursor.execute("SELECT * FROM addr_districts WHERE division_id = " + division_db_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            self.district_sql += "INSERT INTO `city` (`id`, `created`, `updated`, `uuid`, `is_deleted`, `is_active`, `name`, `code`, `other`, `bbs_code`, `state_id`) VALUES ("
            self.district_sql += str(self.district_index) + ", now(), now(), UUID(), 0, 1,'" + str(row[6]).capitalize() + "', '', '', " + str(row[10]) + "," + str(division_id) + ");\n"
            self.process_upozzila(self.district_index, str(row[0]))
            self.district_index += 1

    def process_division(self, country_id):
        mycursor = self.mysql_database.cursor()
        mycursor.execute("SELECT * FROM addr_divisions")
        myresult = mycursor.fetchall()
        for row in myresult:
            self.division_sql += "INSERT INTO `state` (`id`, `created`, `updated`, `uuid`, `is_deleted`, `is_active`, `name`, `code`, `other`, `bbs_code`, `country_id`) VALUES ("
            self.division_sql += str(self.division_index) + ", now(), now(), UUID(), 0, 1,'" + str(row[6]).capitalize() + "', '', '', " + str(row[9]) + ",17);\n"
            self.process_district(self.division_index, str(row[0]))
            self.division_index += 1


bd_geoLocation = BDGeoLocation()
bd_geoLocation.process_division(17)

print("-- BD DIVISION")
print(bd_geoLocation.division_sql)

print("\n\n")
print("-- BD DISTRICT")
print(bd_geoLocation.district_sql)

print("\n\n")
print("-- BD UPOZZILA")
print(bd_geoLocation.upozzila_sql)
