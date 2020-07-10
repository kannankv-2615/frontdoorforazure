import mysql.connector

mydb = mysql.connector.connect(
  host="amptdb.mysql.database.azure.com",
  user="Azureadmin@amptdb",
  password="Password@123",
  database="mysampledb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM inventory")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
