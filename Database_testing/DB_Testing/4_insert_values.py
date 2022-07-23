import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

sql = "insert into Employee2(names, ids, salarys, dept_ids) values (%s, %s, %s, %s)"

records = [("lele", 117, 70000.00, 201),
           ("jile", 118, 80000.00, 205)]

try:
    # inserting the values into the table
    curser.executemany(sql, records)

    # commit the transaction
    myconn.commit()

except:
    myconn.rollback()

print(curser.rowcount, "record inserted!")
myconn.close()
