from datetime import datetime

def generate_date() -> datetime:
    
    #current date and time 
    now: datetime = datetime.now()
    
    #date format change
    date: datetime = now.strftime("%d-%m-%Y %H:%M:%S")
    return date