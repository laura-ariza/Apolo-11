import random 
import logging

logging.basicConfig(filename='device_status.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_device_status() -> str:
    """Generates a random device status.

    Returns:
        str: A random device status from a list of options.
    
    Raises:
        Exception: If an error occurs during device status generation.
    """
    try:
        # List of device status
        option_status: list[str] = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
        
        # Device status randomization 
        device_status: str = random.choice(option_status)
        logging.info("Device status generated successfully.")
        return device_status
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        
