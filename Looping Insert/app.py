import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython"
)

cur = mydb.cursor()

myList = [1,2,3,4]
for row in myList:
   cur.execute("INSERT INTO tesloop (nama) VALUES (%s)" % row)
   mydb.commit()
