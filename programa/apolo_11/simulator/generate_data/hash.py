import hashlib
import logging

logging.basicConfig(filename='hash.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_hash(now_date, value_mission, device, device_status) ->str:
    """This function generates a hash based on the input parameters.

    Args:
        now_date (str): Date of the mission.
        value_mission (str): Mission value.
        device (str): Type of device used.
        device_status (str): Status of the device.

    Returns:
        str: The hash value.
        
    Raises:
        Exception: If an error occurs during hash generation.
    """
    try:
        # Concatenate relevant data to generate the hash
        hash_data = f"{now_date}{value_mission}{device}{device_status}"
        
        # Apply hash SHA-256 to concatenated data
        hash_result = hashlib.sha256(hash_data.encode()).hexdigest()
        logging.info("Hash generated successfully.")
        return hash_result
    except Exception as e:
        logging.error(f"An error occurred: {e}")
