import os.path

from database_connection import *

# database file path
db_file_path = './Users/prakashpandit/Documents/sqlite3/my_db.db'
db_file_path = db_file_path
if not os.path.exists(db_file_path):
    os.mkdir(db_file_path)

# create database connection
db_conn = create_connection(db_file_path)

# create table
create_table = execute_sql(db_conn, """ create table if not exists users(
        id int,
        name varchar(100),
        age int,
        email varchar(100)
    )""")

# insert data into table
insert_query = ("insert into users(id , name, age , email) values (1,'chris',25, 'chris@gmail.com'),(2,'amy',30, "
                "'amy@gmail.com'),(3,'john',35, 'john@gmail.com')")
print(execute_sql(db_conn, insert_query))

# select data from table
select_query = "select * from users"
print(execute_sql(db_conn, select_query))
