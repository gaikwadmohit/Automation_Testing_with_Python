import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

curser.execute("update Employee1 set salary=27000.00 where name='moni'")
myconn.commit()