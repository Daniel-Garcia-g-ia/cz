import os
from datetime import datetime, timedelta

def create_dir_year (url=str):
    '''
    This fucntion creates a directoy for the year
    
    Args:
        url (string): The URL for the location where the directory will be created
        
    Return: 
        string:Directory path created.
        bolean: True or False, if the path has been created
    
    
    '''
    
    
    today = datetime.now()
    year = today.strftime('%Y')
    
    directory= f"{url}/{year}"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return (directory,True)
        
    else:
        return (directory,False)
    
    

def create_dir_month (url=str):
    
    '''
    This fucntion creates a directoy for the month
    
    Args:
        url (string): The URL for the location where the directory will be created
        
    Return: 
        string:Directory path created.
        bolean: True or False, if the path has been created   
    
    '''
    today = datetime.now()
    year= today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d') 
    
    directory= f"{url}/{year}/{month}"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return (directory, day, True)
        
    else:
        return (directory, day, False)
    
def create_dir_day(url=str, turn=int):

    '''
    This function creates a directory for the current day or the previous day based on the turn.
    
    Args:
        url (string): The base URL or path where the directory will be created.
        turn (int): The current shift number. If the turn is 3, the directory for the previous day will be created.
        
    Returns: 
        tuple: A tuple containing:
            - string: The full directory path created.
            - string: The day (current or previous) for which the directory was created.
            - boolean: True if the directory was created, False if it already existed.
    
    Description:
        The function determines whether to create a directory for the current day or the previous day, based on the value of the `turn` parameter. 
        - If `turn == 3`, the directory for the previous day is created.
        - For any other `turn`, the directory for the current day is created.
        
        If the directory does not already exist at the specified `url`, it will be created. The function returns the path of the directory, the day, and a boolean indicating whether the directory was newly created or already existed.
    '''
    
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)    
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    day_prev = yesterday.strftime('%d')
    
    
    if turn == 3:
        directory= f"{url}/{year}/{month}/{day_prev}"
        if not os.path.exists(directory):
            os.makedirs(directory)
            return (directory, day_prev, True)
        else:
            return (directory, day_prev, False)       
        
    else:
        directory= f"{url}/{year}/{month}/{day}"  
            
        if not os.path.exists(directory):
            os.makedirs(directory)
            return (directory, day, True)
            
        else:
            return (directory, day, False)    
    
    
    
def create_dir_yesterday(url=str, filename=str):
    '''
    This function creates a directory for the previous day and checks if a specific file exists in the created summary directory.

    Args:
        url (str): The URL for the location where the directory will be created.
        filename (str): The name of the file (without extension) to check for in the summary directory. The file is assumed to be an Excel file (.xlsx).

    Returns:
        tuple:
            - string: Directory path created for the previous day in the format 'url/YYYY/MM/DD'.
            - string: Summary directory path for the previous month in the format 'url/YYYY/MM'.
            - string: Day of the directory creation (e.g., "04").
            - string: Month in text format (e.g., "October").
            - boolean: True if the directory for the previous day was created, False if it already existed.
            - boolean: True if the file with the specified name and '.xlsx' extension exists in the summary directory, False otherwise.

    Example:
        >>> create_dir_yesterday('/path/to/directory', 'example_file')
        ('/path/to/directory/2024/10/04', '/path/to/directory/2024/10', '04', 'October', True, False)

    The function performs the following steps:
        1. Calculates the date for the previous day and uses it to determine the directory path (year/month/day) and summary path (year/month).
        2. Checks if the directory for the previous day exists. If not, it creates the directory.
        3. Verifies if a file named 'filename_Month.xlsx' (e.g., 'example_file_October.xlsx') exists in the summary directory.
        4. Returns the paths, day, month, whether the directory was created, and whether the file exists.

    '''   
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    year = yesterday.strftime('%Y')
    month = yesterday.strftime('%m')
    month_text = yesterday.strftime('%B')
    day = yesterday.strftime('%d') 
    
    directory_turn_report = f"{url}/{year}/{month}/{day}"
    directory_summary_report = f"{url}/{year}/{month}"
    
    # Check if the directory exists and create it if not
    if not os.path.exists(directory_turn_report):
        os.makedirs(directory_turn_report)
        file_exists = False
        directory_created = True
    else:
        directory_created = False

    # Check if the specific file exists in the directory
    file_path = os.path.join(directory_summary_report, f'{filename}_{month_text}.xlsx')
    print(file_path)
    if os.path.exists(file_path):
        file_exists = True
    else:
        file_exists = False
    
    return (directory_turn_report, directory_summary_report, day, month_text, directory_created, file_exists)


def create_dir_day_now(url:str, filename:str ):
    

    today = datetime.now()    
    year = today.strftime('%Y')
    month = today.strftime('%m')
    month_text = today.strftime('%B')
    day = today.strftime('%d') 
    
    directory_turn_report = f"{url}/{year}/{month}/{day}"
    directory_summary_report = f"{url}/{year}/{month}"
    
    # Check if the directory exists and create it if not
    if not os.path.exists(directory_turn_report):
        os.makedirs(directory_turn_report)
        file_exists = False
        directory_created = True
    else:
        directory_created = False

    # Check if the specific file exists in the directory
    file_path = os.path.join(directory_summary_report, f'{filename}_{month_text}.xlsx')
    print(file_path)
    if os.path.exists(file_path):
        file_exists = True
    else:
        file_exists = False
    
    return (directory_turn_report, directory_summary_report, day, month_text, directory_created, file_exists)
    
