import mysql.connector


def test_show_database():

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595")
    curser = myconn.cursor()
    curser.execute("show databases")
    for db in curser:
        print(db)

def test_create_database():
    import mysql.connector

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595")
    curser = myconn.cursor()
    curser.execute("create database PythonDB5")

def test_create_table():

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595",database="PythonDB5")
    curser = myconn.cursor()
    curser.execute("create table Employee2(names varchar(20) not null, ids int(20) not null primary key, salarys float "
                   "not null, Dept_ids int not null)")


def test_insert_table():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB5")
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


def test_where():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB5")
    curser = myconn.cursor()

    curser.execute("select * from Employee2 ") #--all select
    # curser.execute("select * from Employee1 where name='moni'")  #--select name
    # curser.execute("SELECT * FROM Employee1 WHERE name = 'soni' AND id > 100;") #--use and
    # curser.execute("SELECT * FROM Employee2 WHERE names = 'bele' or ids <100;   ")  #--use or
    # curser.execute("SELECT * FROM Employee2 WHERE (names = 'bele' and ids=115) or (dept_ids <100)   ") #--use and or
    # curser.execute("SELECT name, salary FROM Employee1 WHERE EXISTS (SELECT * FROM Employee2  WHERE "
    #                "Employee1.dept_id = Employee2.Dept_ids)")   #--use EXIST

    # curser.execute("SELECT * FROM Employee2 WHERE ids not between 114 and 117 ")  #--use not betweeen
    # curser.execute("SELECT * FROM Employee2 WHERE names != 'bele';  ")  #--use not equall

    result = curser.fetchall()
    # result=curser.fetchone()
    print(" name,  id,  salary,  dept_id")
    for r in result:
        print(r)

def test_update():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB5")
    curser = myconn.cursor()

    curser.execute("update Employee2 set salarys=78000.00 where names='lele'  ")
    # myconn.commit()

def test_delete():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB5")
    curser = myconn.cursor()

    curser.execute("delete from Employee2 where name='lele'")
    myconn.commit()
    print("Record deleted !!!!!!")


def test_alter_table():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595", database="PythonDB5")
    curser = myconn.cursor()

    # Add column in table
    curser.execute("alter table Employee2 add age int(10)")

    # Drop column age
    # curser.execute("alter table Employee2 drop column age")

    # Rename column in table
    # curser.execute("alter table Employee2 change column age ages int (20)")

    # Rename table name
    # curser.execute("alter table Employee2 rename to Employee2.1")

    # arrange in desc order by id
    # curser.execute("DESC Employee2")



