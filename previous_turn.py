import os
from dotenv import load_dotenv  
from sql_query import fetch_records_by_date  
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
URL_SUMMARY_DIRECTORY = os.getenv('URL_SUMMARY_DIRECTORY')
NAME_FILE_REPORT = os.getenv('NAME_FILE_REPORT')



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

        path_turn_report_day, day, created = create_dir_day(URL_SUMMARY_DIRECTORY, turn)
        
        file_turn_report_excel(URL_REPORT,path_turn_report_day, turn, day, records)
        
       

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
