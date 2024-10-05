import os
from dotenv import load_dotenv  
from src.sql.sql_query import fetch_records_by_date  
from scripts.get_date import get_current_day as date
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
URL_YEAR_DIRECTORY = os.getenv('URL_YEAR_DIRECTORY')
URL_SUMMARY_DIRECTORY = os.getenv('URL_SUMMARY_DIRECTORY')
NAME_FILE_REPORT = os.getenv('NAME_FILE_REPORT')


def main():
    # set date turn now
    start_time, end_time= date() 
    
    # Parameter for the query
    table_name = DB_TABLE  # table name
    start_date = f'{start_time}'  # start time turn now
    end_date = f'{end_time}'  # end time turn  now 
    

    try:
        # call the función fetch_records_by_date
        records = fetch_records_by_date(DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD, table_name, start_date, end_date,'Created')

       
        path_summary_day_report, path_summary_report, day, month_text, path_created, file_exists = create_dir_day_now(URL_SUMMARY_DIRECTORY,NAME_FILE_REPORT)     
        
        if file_exists:
            name_file= f'{NAME_FILE_REPORT}_{month_text}.xlsx'
            path_update_file= f'{path_summary_report}/{name_file}'            
            file_day_summary(path_update_file, path_summary_report, records, day, month_text)
            print('update file succefull')
        else:
            file_day_summary(URL_REPORT, path_summary_report, records, day, month_text)
            print('created file succefull')
       

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
