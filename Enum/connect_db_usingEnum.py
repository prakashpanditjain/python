import sqlite3  # For SQLite database connection
from enum import StrEnum  # For defining string-based Enum types
from typing_extensions import Optional  # For type hinting optional return types

# Define an Enum to represent supported database types
class DatabaseType(StrEnum):
    SQLITE = "SQLite"  # Represents SQLite database
    MYSQL = "MySQL"  # Represents MySQL database (placeholder for future implementation)

# Class to manage database connections
class DatabaseConnectionManager:
    def __init__(self, db_type: DatabaseType, db_name: str):
        """
        Initialize the DatabaseConnectionManager with a database type and name.

        :param db_type: Enum value specifying the type of database (e.g., SQLite or MySQL).
        :param db_name: Name of the database file (for SQLite) or connection string.
        """
        self.db_type = db_type  # Database type (from the Enum)
        self.db_name = db_name  # Database name or file name
        self.connection = None  # Placeholder for the database connection object

    def connect(self):
        """
        Establish a connection to the database based on the specified type.
        """
        if self.db_type == DatabaseType.MYSQL.value:
            # Placeholder: MySQL support is not implemented
            print(f"{self.db_type} support is not implemented yet ...")
        elif self.db_type == DatabaseType.SQLITE.value:
            # Connect to SQLite database
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to {self.db_type} database: {self.db_name}")
        else:
            # Raise an error if the database type is unsupported
            raise ValueError(f"Unsupported datatype : {self.db_type.value}")

    def get_connection(self) -> Optional[sqlite3.Connection]:
        """
        Get the database connection object. If no connection exists, create one.

        :return: SQLite connection object (or None if connection fails).
        """
        if not self.connection:
            self.connect()  # Establish connection if not already connected
        return self.connection

    def close_connection(self):
        """
        Close the database connection if it exists.
        """
        if self.connection:
            self.connection.close()
            print(f"Connection to the {self.db_type} database has closed")

# Function to perform database operations
def perform_database_operation(db_manager: DatabaseConnectionManager):
    """
    Perform a series of database operations:
    - Create a 'users' table if it doesn't already exist.
    - Insert sample data into the table.
    - Fetch and display the data.

    :param db_manager: Instance of DatabaseConnectionManager to interact with the database.
    """
    conn = db_manager.get_connection()  # Get the database connection
    cursor = conn.cursor()  # Create a cursor for executing SQL queries

    # Create the 'users' table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            email TEXT NOT NULL UNIQUE
        )
    ''')
    print("Table created successfully")

    # Sample data to insert into the table
    users = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
    ]

    # Insert the sample data, ignoring duplicate entries
    cursor.executemany("INSERT OR IGNORE INTO users (id, name, email) VALUES (?, ?, ?)", users)
    conn.commit()  # Commit the transaction
    print("Data inserted successfully")

    # Retrieve and display all rows from the 'users' table
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)  # Print each row (id, name, email)

    db_manager.close_connection()  # Close the database connection

# Main function to initialize and run the database operations
def main():
    """
    Main entry point for the program:
    - Sets up the database type and name.
    - Initializes the DatabaseConnectionManager.
    - Executes the database operations.
    """
    db_type = DatabaseType.SQLITE  # Specify the database type (SQLite)
    db_name = 'test_db'  # Specify the database file name

    db_manager = DatabaseConnectionManager(db_type, db_name)  # Initialize the connection manager
    perform_database_operation(db_manager)  # Perform database operations

# Execute the main function when the script is run
if __name__ == '__main__':
    main()