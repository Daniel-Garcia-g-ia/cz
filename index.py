import os
from dotenv import load_dotenv  
""" from sql_query import fetch_records_by_date   """
from scripts.get_date import get_current_turno as date

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura las variables de conexión usando os.getenv
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_TABLE = os.getenv('DB_TABLE')


def main():
    # set date turn now
    start_time, end_time = date() 
    
    # Parameter for the query
    table_name = DB_TABLE  # table name
    start_date = f'{start_time}'  # start time turn now
    end_date = f'{end_time}'  # end time turn  now 
    
    

    """ try:
        # call the función fetch_records_by_date
        records = fetch_records_by_date(DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD, table_name, start_date, end_date)

        
        print(records)

    except Exception as e:
        print(f"An error occurred: {e}") """


if __name__ == '__main__':
    main()
