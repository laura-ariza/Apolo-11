import random 
import logging

logging.basicConfig(filename='device.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_device() -> str:
    """Generate a random device type from a predefined list.

    Returns:
        str: Randomly selected device type from options.
    
    Raises:
        Exception: If an error occurs during device generation.
    """
    try:
        # List of device options 
        option_device: list[str] = ["satellites", "airplanes", "suits", "vehicles"]
        
        # Device randomization
        device_type: str = random.choice(option_device)
        logging.info("Device generated successfully.")
        return device_type
    except Exception as e:
        logging.error(f"An error occurred: {e}")