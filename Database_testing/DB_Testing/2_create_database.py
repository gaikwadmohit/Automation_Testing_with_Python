import mysql.connector

def create_database():
    import mysql.connector

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="gaikwad595")
    curser = myconn.cursor()
    curser.execute("create database PythonDB3")


create_database()
