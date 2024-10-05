from datetime import datetime, timedelta

from datetime import datetime, timedelta

def get_current_turno_prev():
    """
    Determine the current turno (shift) and the previous turno based on the current time.

    Returns:
        tuple: 
            - string: Start time of the previous turno in 'YYYY-mm-dd HH:MM:SS' format.
            - string: End time of the previous turno in 'YYYY-mm-dd HH:MM:SS' format.
            - int: Number of the previous turno.
    
    Description:
        This function divides the day into three turnos (shifts):
        - Turno 1: 06:00 - 14:00
        - Turno 2: 14:00 - 22:00
        - Turno 3: 22:00 - 06:00 (overnight, spanning two days)
        
        It determines the current time and calculates the current and previous turnos start and end times.
        The previous turno is returned along with its start and end times.
    
    Turnos:
        - Turno 1: Starts at 06:00 and ends at 14:00
        - Turno 2: Starts at 14:00 and ends at 22:00
        - Turno 3: Starts at 22:00 and ends at 06:00 (next day)

    Returns:
        A tuple with the following elements:
        - Start time of the previous turno in the format 'YYYY-mm-dd HH:MM:SS'.
        - End time of the previous turno in the format 'YYYY-mm-dd HH:MM:SS'.
        - The previous turno number (1, 2, or 3).
    """
    now = datetime.now()
    current_time = now.time()  # Set current time

    # Define the turno schedules
    turno_1_start = datetime.strptime('06:00:00', '%H:%M:%S').time()
    turno_1_end = datetime.strptime('14:00:00', '%H:%M:%S').time()

    turno_2_start = datetime.strptime('14:00:00', '%H:%M:%S').time()
    turno_2_end = datetime.strptime('22:00:00', '%H:%M:%S').time()

    turno_3_start = datetime.strptime('22:00:00', '%H:%M:%S').time()
    turno_3_end = (datetime.strptime('06:00:00', '%H:%M:%S') + timedelta(days=1)).time()  # Add a day to cover the night shift

    # Determine the current turno
    if turno_1_start <= current_time < turno_1_end:
        current_turno = 1
        start_time = datetime.combine(now.date(), turno_1_start)
        end_time = datetime.combine(now.date(), turno_1_end)

        # Determine previous turno (Turno 3 from the previous day)
        prev_start_time = datetime.combine(now.date() - timedelta(days=1), turno_3_start)
        prev_end_time = datetime.combine(now.date(), turno_1_start)
        prev_turno = 3

    elif turno_2_start <= current_time < turno_2_end:
        current_turno = 2
        start_time = datetime.combine(now.date(), turno_2_start)
        end_time = datetime.combine(now.date(), turno_2_end)

        # Previous turno is Turno 1
        prev_start_time = datetime.combine(now.date(), turno_1_start)
        prev_end_time = datetime.combine(now.date(), turno_1_end)
        prev_turno = 1

    else:
        current_turno = 3
        start_time = datetime.combine(now.date(), turno_3_start)
        end_time = datetime.combine(now.date() + timedelta(days=1), turno_3_end)

        # Previous turno is Turno 2
        prev_start_time = datetime.combine(now.date(), turno_2_start)
        prev_end_time = datetime.combine(now.date(), turno_2_end)
        prev_turno = 2

    """ return (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), current_turno), \
           (prev_start_time.strftime('%Y-%m-%d %H:%M:%S'), prev_end_time.strftime('%Y-%m-%d %H:%M:%S'), prev_turno) """
           
    return (prev_start_time.strftime('%Y-%m-%d %H:%M:%S'), prev_end_time.strftime('%Y-%m-%d %H:%M:%S'), prev_turno)


def get_current_yesterday():
    """
    Determine the start and end times for the previous day (yesterday).

    Returns:
        tuple: A tuple containing:
            - string: The start time of yesterday in 'YYYY-mm-dd HH:MM:SS' format (00:00:00).
            - string: The end time of yesterday in 'YYYY-mm-dd HH:MM:SS' format (23:59:59).
    
    Description:
        This function calculates the start and end times for the previous day (yesterday).
        - The start time is set to '00:00:00' of the previous day.
        - The end time is set to '23:59:59' of the previous day.
        
        The function returns these times formatted as 'YYYY-mm-dd HH:MM:SS'.
    """   
    
    today = datetime.now()   

    start_time = datetime.strptime('00:00:00', '%H:%M:%S').time()
    end_time = datetime.strptime('23:59:59', '%H:%M:%S').time()
    
    start_date = datetime.combine(today.date()-timedelta(days=1),start_time)
    end_date = datetime.combine(today.date()-timedelta(days=1), end_time)
    
    return start_date.strftime('%Y-%m-%d %H:%M:%S'), end_date.strftime('%Y-%m-%d %H:%M:%S')
    
def get_current_day():
    """
    Determine the start and end times for the current day.

    Returns:
        tuple: A tuple containing:
            - string: The start time of today in 'YYYY-mm-dd HH:MM:SS' format (00:00:00).
            - string: The end time of today in 'YYYY-mm-dd HH:MM:SS' format (23:59:59).
    
    Description:
        This function calculates the start and end times for the current day.
        - The start time is set to '00:00:00' of today.
        - The end time is set to '23:59:59' of today.
        
        The function returns these times formatted as 'YYYY-mm-dd HH:MM:SS'.
    """  
    
    today = datetime.now()   

    start_time = datetime.strptime('00:00:00', '%H:%M:%S').time()
    end_time = datetime.strptime('23:59:59', '%H:%M:%S').time()
    
    start_date = datetime.combine(today.date(),start_time)
    end_date = datetime.combine(today.date(), end_time)
    
    return start_date.strftime('%Y-%m-%d %H:%M:%S'), end_date.strftime('%Y-%m-%d %H:%M:%S')
    