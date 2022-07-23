import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

try:
    curser.execute("delete from Employee1 where dept_id =201")
    # myconn.commit()
    print("Deleted !")
except:
    print("Can't delete !")
    #-----------------------if not deleted the it directly do undo
    myconn.rollback()

myconn.close()