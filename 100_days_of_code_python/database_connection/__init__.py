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
