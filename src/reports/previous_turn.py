import os
from dotenv import load_dotenv  
from src.sql.sql_query import fetch_records_by_date  
from scripts.get_date import get_current_turno_prev as date
from scripts.file import *
from scripts.create_dir import *

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura las variables de conexión usando os.getenv
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_TABLE = os.getenv('DB_TABLE')
URL_REPORT = os.getenv('URL_REPORT')
URL_REPORT = os.getenv('URL_REPORT')
URL_YEAR_DIRECTORY = os.getenv('URL_YEAR_DIRECTORY')


def main():
    # set date turn now
    start_time, end_time, turn = date() 
    
    # Parameter for the query
    table_name = DB_TABLE  # table name
    start_date = f'{start_time}'  # start time turn now
    end_date = f'{end_time}'  # end time turn  now 
    

    try:
        # call the función fetch_records_by_date
        records = fetch_records_by_date(DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD, table_name, start_date, end_date,'Created')

        year_directory= create_dir_year(URL_YEAR_DIRECTORY)
        month_directory = create_dir_month(URL_YEAR_DIRECTORY)
        day_directory, status = create_dir_day(URL_YEAR_DIRECTORY)
        
        file_turn_report_excel(URL_REPORT,day_directory, turn, records)
        
       

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
