from xml.etree.ElementTree import SubElement
import pingSubnet
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (ip) VALUES (%s)"
val = (pingSubnet.hostalive)
mycursor.execute(val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
