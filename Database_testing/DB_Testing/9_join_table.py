import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

# curser.execute("select Employee1.id, Employee1.name, Employee1.salary, Employee2.dept_ids, Employee2.names from "
#                "Employee1 join Employee2 on Employee2.dept_ids = Employee1.Dept_id")

# Right join
# curser.execute("select Employee1.id, Employee1.name, Employee1.salary, Employee2.dept_ids, Employee2.names from "
#                "Employee2 right join Employee1 on Employee2.dept_ids = Employee1.Dept_id")

#Left_Join
curser.execute("select Employee1.id, Employee1.name, Employee1.salary, Employee2.dept_ids, Employee2.names from "
               "Employee2 left join Employee1 on Employee2.dept_ids = Employee1.Dept_id")


print("  id : name :  salary :dept_id: names")
for row in curser:
    print(row)
