import sqlite3

def create_connection(db_file_path):
    """ create a database connection to the SQLite database
        specified by db_file_path
    :param db_file_path: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        conn = conn.cursor()
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def execute_sql(conn, query):
    """
    Execute a single query
    """
    result = conn.execute(query)
    return result.fetchall()

def read_csv(file_path):
    """
    Read a CSV file and return its content as a list of tuples
    """
    import csv
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [tuple(row) for row in csv_reader]
    return data

def create_pandas_df(data, columns, header=True):
    """
    Create a pandas DataFrame from data and column names
    """
    import pandas as pd
    # give give header as true if the first row is header
    if header:
        data = data[1:]  # Skip the first row if it's a header
    df = pd.DataFrame(data, columns=columns)
    return df
