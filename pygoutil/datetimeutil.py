from datetime import datetime

def timetaken(before_date, current=datetime.now()):
    result = current - before_date
    if result.days:
        time_taken = '{} dia(s)'.format(result.days)
    else:
        seconds = result.seconds
        if seconds >= 3600:
            time_taken = '{} hora(s)'.format(int(seconds / 3600))
        elif seconds >= 60:
            time_taken = '{} minuto(s)'.format(int(seconds / 60))
        else:
            time_taken = '{} segundo(s)'.format(seconds)
    return time_taken