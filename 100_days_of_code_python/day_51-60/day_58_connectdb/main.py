import psycopg2
import pandas as pd

# Database connection details
DB_NAME = "mydatabase"
DB_USER = "prakashpandit"
DB_PASSWORD = "******"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor object
    cursor = conn.cursor()

    # SQL query to fetch data
    query = "SELECT * FROM employees;"

    # Load data into a Pandas DataFrame
    df = pd.read_sql(query, conn)

    columns = ", ".join(df.columns)
    print(columns)

    placeholders= ", ".join(["%s"] * len(df.columns))
    print(placeholders)

    records = [tuple(row) for row in df.itertuples(index=False, name=None)]
    # print(records)

    truncate_query = f"TRUNCATE TABLE employee_copy;"
    cursor.execute(truncate_query)
    conn.commit()

    insert_query = f"insert into employee_copy ({columns}) VALUES ({placeholders})"

    if records:
        cursor.executemany(insert_query, records)
        print("insert executed succesfully")
        conn.commit()

    # Display the DataFrame
    # print(df)

    # Close the connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to database:", e)