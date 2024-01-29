from datetime import datetime
import logging

logging.basicConfig(filename='date.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_date() -> str:
    """This function generates a current date and time in the
    format of "dd-mm-yyyy HH:MM:SS"
    Returns:
        str: A current date and time in the given format

    Raises:
        Exception: If an error occurs during date generation.
    """
    try:
        # Current date and time
        now: datetime = datetime.now()

        # Date format change
        date: str = now.strftime("%d-%m-%Y %H:%M:%S")
        logging.info("Date generated successfully.")
        return date
    except Exception as e:
        logging.error(f"An error occurred: {e}")
