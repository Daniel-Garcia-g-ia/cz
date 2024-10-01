import os
from datetime import datetime

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
    
    directory= f"{url}/{year}/{month}"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return (directory, True)
        
    else:
        return (directory,False)
    
def create_dir_day(url=str):

    '''
    This fucntion creates a directoy for the day
    
    Args:
        url (string): The URL for the location where the directory will be created
        
    Return: 
        string:Directory path created.
        bolean: True or False, if the path has been created   
    
    '''
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d') 
    
    directory= f"{url}/{year}/{month}/{day}"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return (directory,True)
        
    else:
        return (directory,False)    

    
    
