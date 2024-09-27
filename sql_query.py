import pyodbc

def fetch_records_by_date(server: str, database: str, username: str, password: str, table: str, start_date: str, end_date: str, order_by: str):
    """
    Fetch records from a given SQL Server database table, filtered by date and time range.

    Args:
        server (str): The server address, including the port.
        database (str): The name of the database to connect to.
        username (str): The username for the database authentication.
        password (str): The password for the database authentication.
        table (str): The name of the table from which to retrieve the records.
        start_date (str): The starting date and time (in 'dd-mm-yyyy HH:MM:SS' format) to filter the records.
        end_date (str): The ending date and time (in 'dd-mm-yyyy HH:MM:SS' format) to filter the records.
        order_by (str): The column by which to order the results, defaults to 'Created'.

    Returns:
        list: A list of lists, where each inner list represents a row from the query result.

    Raises:
        Exception: If there is an issue with the database connection or executing the query.
    """
    
    # String connection to the SQL Server database
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    try:
        # Establish the connection
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to SQL Server database")
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # SQL query to fetch records filtered by a date and time range, ordered by a specific column
        query = f"""
        SELECT * FROM {table} 
        WHERE {order_by} BETWEEN ? AND ? 
        ORDER BY {order_by} DESC
        """
        
        # Execute the query with the start and end dates as parameters
        cursor.execute(query, (start_date, end_date))
        
        # Fetch all results and convert to a list of lists
        rows = cursor.fetchall()
        result = [list(row) for row in rows]  
        
       
        cursor.close()
        conn.close()
        
        return result
    
    except Exception as e:
        # Raise an exception if there's an issue during the connection or query execution
        raise Exception(f"Error during database connection or query execution: {e}")


