import mysql.connector


def create_table():

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595",database="PythonDB3")
    curser = myconn.cursor()
    curser.execute("create table Employee2(names varchar(20) not null, ids int(20) not null primary key, salarys float "
                   "not null, Dept_ids int not null)")



create_table()