from datetime import datetime

def generate_date() -> str:  # Change the name of the function
    """This function generates a current date and time in the
    format of "dd-mm-yyyy HH:MM:SS"
    Returns:
        str: A current date and time in the given format
    """
    try:
        # Current date and time
        now: datetime = datetime.now()

        # Date format change
        date: str = now.strftime("%d-%m-%Y %H:%M:%S")
        return date
    except Exception as e:
        print(f"An error occurred: {e}")
