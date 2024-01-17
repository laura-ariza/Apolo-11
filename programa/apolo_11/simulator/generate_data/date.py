from datetime import datetime


def gen_date() -> datetime:  # change the name of the function

    # current date and time
    now: datetime = datetime.now()

    # date format change
    date: datetime = now.strftime("%d-%m-%Y %H:%M:%S")
    return date
