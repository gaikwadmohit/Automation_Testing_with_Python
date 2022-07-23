import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

#Add column in table
curser.execute("alter table Employee2 add age int(10)")

#Drop column age
# curser.execute("alter table Employee2 drop column age")

#Rename column in table
# curser.execute("alter table Employee2 change column age ages int (20)")

#Rename table name
# curser.execute("alter table Employee2 rename to Employee2.1")

#arrange in desc order by id
# curser.execute("DESC Employee2")

