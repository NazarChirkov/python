import pymysql
from config import host, user, password, db_name
from datetime import datetime

def create_table(connection, name):
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE %s (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) DEFAULT 'no name',
        major VARCHAR(20) NOT NULL,
        date VARCHAR(32) UNIQUE
        );
        """ % (name)
        cursor.execute(create_table_query)
        print("Table created seccesfully")
def create_user(connection,table,name,major):
        cursor = connection.cursor()
        create_user_query = """INSERT INTO %s(name,major,date) VALUES ('%s','%s','%s')""" % (table,name,major,datetime.now())
        cursor.execute(create_user_query)
        connection.commit()
        print("User created seccesfully")
def drop_table(connection, table):
        cursor = connection.cursor()
        delete_table_query = """DROP TABLE %s""" %(table)
        cursor.execute(delete_table_query)
        connection.commit()
        print("Table deleted seccesfully")
def show_all_rows(connection,table):
        cursor = connection.cursor()
        cursor.execute("""SELECT SUM(employee.salary) AS SALARY, branch.branch_name AS NAME
                        FROM employee 
                        JOIN branch ON employee.branch_id = branch.branch_id
                        GROUP BY employee.branch_id;
                        """ )
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("Rows show seccesfully")
def update_row(connection,table,name_of_row):
        cursor = connection.cursor()
        cursor.execute("""UPDATE %s
                        SET major = 'Ma'
                        WHERE major = '%s'
        """ % (table, name_of_row))
        print("Rows update seccesfully")
def do_smth(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    print("seccesfully")
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
    #create_table(connection,"students")
    #create_user(connection,"students", "Oleg", "UK")
    #update_row(connection,"students","Maths")
    #drop_table(connection, "branch")
    #drop_table(connection,"employee")
    #do_smth(connection,"""SELECT * FROM Employeer""")
    show_all_rows(connection,"Employeer")
    connection.close()
 except Exception as ex:
    print(ex)
mySQL()