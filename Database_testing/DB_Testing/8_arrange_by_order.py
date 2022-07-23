import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

# curser.execute("select name, id, salary, dept_id from Employee1 order by salary")
curser.execute("select name, id, salary, dept_id from Employee1 order by salary desc")


result = curser.fetchall()
# result=curser.fetchone()
print(" name,  id,  salary,  dept_id")
for r in result:
    print(r)
