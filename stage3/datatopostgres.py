import psycopg2
import csv

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "tree0112", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE res1(
           TYPE TEXT ,
           FEATURES_TYPE TEXT, 
           PLACE TEXT,
           PLACE_TYPE TEXT,
           PARENT TEXT,
           GEOMETRY TEXT,
           LATITUDE REAL NOT NULL,
           LONGITUDE REAL NOT NULL);
             ''')
#print ("Table created successfully")
cur.execute('''COPY res1
FROM '/tmp/database.csv' DELIMITER ',' CSV HEADER;''')
#cur.execute("select features_geometry_coordinates_lat from res where res.feature_properties_name="Gurgaon";")
#row=curs.fetchall()
#print(rows)

conn.commit()
conn.close()
