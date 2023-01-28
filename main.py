import pymysql
from config import host, user, password, db_name
from datetime import datetime

def create_table(connection):
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(20),
        major VARCHAR(20)
        );
        """
        print("Table created seccesfully")
def create_user(connection):
        cursor = connection.cursor()
        connection.commit()
def show_all_rows(connection):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM userB""")
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
    connection.close()
 except Exception as ex:
    print(ex)
mySQL()