import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

curser.execute("delete from Employee1 where name='moni'")
myconn.commit()
print("Record deleted !!!!!!!!!!!!!!")