import psycopg2

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "demon0112", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE geogaphic
      (KEY 	CHAR(9)    NOT NULL,
      PLACE_NAME     TEXT    NOT NULL,
      ADMIN_NAME1    TEXT     NOT NULL,
      LATITUDE        REAL  ,
      LONGITUDE       REAL  ,
      ACCURACY  INT  );''')
print ("Table created successfully")
cur.execute('''COPY geogaphic
FROM '/tmp/IN.csv' DELIMITER ',' CSV HEADER;''')

conn.commit()
conn.close()
