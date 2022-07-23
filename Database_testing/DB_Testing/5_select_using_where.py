import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB3")
curser = myconn.cursor()

# curser.execute("select * from Employee1 ") #--all select
# curser.execute("select * from Employee1 where name='moni'")  #--select name
# curser.execute("SELECT * FROM Employee1 WHERE name = 'soni' AND id > 100;") #--use and
# curser.execute("SELECT * FROM Employee2 WHERE names = 'bele' or ids <100;   ")  #--use or
# curser.execute("SELECT * FROM Employee2 WHERE (names = 'bele' and ids=115) or (dept_ids <100)   ") #--use and or
# curser.execute("SELECT name, salary FROM Employee1 WHERE EXISTS (SELECT * FROM Employee2  WHERE "
#                "Employee1.dept_id = Employee2.Dept_ids)")   #--use EXIST

# curser.execute("SELECT * FROM Employee2 WHERE ids not between 114 and 117 ")  #--use not betweeen
# curser.execute("SELECT * FROM Employee2 WHERE names != 'bele';  ")  #--use not equall

result=curser.fetchall()
# result=curser.fetchone()
print(" name,  id,  salary,  dept_id")
for r in result:
    print(r)