from datetime import datetime

def get_time():
    """
    Returns the current time formatted as 'HH hours MM minutes'.
    """
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes")
    return current_time
