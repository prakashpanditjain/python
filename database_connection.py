import psycopg2

import psycopg2

# Connection parameters
db_host = '172.18.0.2'  # Docker container IP or hostname
db_port = '5432'  # PostgreSQL default port
db_name = 'airflow'
db_user = 'airflow'
db_password = 'airflow'

# Establish connection
try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("Connected to PostgreSQL database!")

    # Perform operations here, such as executing queries or fetching data

    # Remember to close the connection when done
    connection.close()
    print("Connection closed.")
except Exception as e:
    print("Error:", e)

