import pymysql
from config import host, user, password, db_name
from datetime import datetime

def create_table(connection):
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) DEFAULT 'no name',
        major VARCHAR(20) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        print("Table created seccesfully")
def create_user(connection,table,name,major):
        cursor = connection.cursor()
        create_user_query = """INSERT INTO %s(name,major) VALUES ('%s','%s')""" % (table,name,major)
        cursor.execute(create_user_query)
        connection.commit()
def show_all_rows(connection):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM students""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
def mySQL():
 try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    create_user(connection,"students", "Oleg", "UK")
    show_all_rows(connection)
    connection.close()
 except Exception as ex:
    print(ex)
mySQL()