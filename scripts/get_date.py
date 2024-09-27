from datetime import datetime, timedelta

def get_current_turno():
    """
    Determine the current turno based on the current time.

    Returns:
        tuple: start and end times for the current turno and date in 'YYYY-MM-DD HH:MM:SS' format.
    """
    now = datetime.now()
    current_time = now.time()  # set current time now
    # define the turn
    turno_1_start = datetime.strptime('06:00:00', '%H:%M:%S').time()
    turno_1_end = datetime.strptime('14:00:00', '%H:%M:%S').time()
    
    turno_2_start = datetime.strptime('14:00:00', '%H:%M:%S').time()
    turno_2_end = datetime.strptime('22:00:00', '%H:%M:%S').time()

    turno_3_start = datetime.strptime('22:00:00', '%H:%M:%S').time()
    turno_3_end = (datetime.strptime('06:00:00', '%H:%M:%S') + timedelta(days=1)).time()  # add a day

    # Determinar el turno actual
    if turno_1_start <= current_time < turno_1_end:
        start_time = datetime.combine(now.date(), turno_1_start)
        end_time = datetime.combine(now.date(), turno_1_end)
        return start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')
    elif turno_2_start <= current_time < turno_2_end:
        start_time = datetime.combine(now.date(), turno_2_start)
        end_time = datetime.combine(now.date(), turno_2_end)
        return start_time.strftime('%Y-%m-%d %H:%M:%S'),end_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        start_time = datetime.combine(now.date(), turno_3_start)
        end_time = datetime.combine(now.date() + timedelta(days=1), turno_3_end) 
        return start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')


