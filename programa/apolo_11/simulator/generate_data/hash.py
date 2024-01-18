#https://docs.python.org/es/3/library/hashlib.html
#Hashlib:this module implements a common interface to many different secure hash and message digest algorithms.
import hashlib

def generate_hash(now_date, value_mission, device, device_status) ->str:
    """This function generates a hash based on the input parameters.

    Args:
        now_date (str): _description_
        value_mission (str): _description_
        device (str): _description_
        device_status (str): _description_

    Returns:
        str: The hash value.
    """
    try:
        # Concatenate relevant data to generate the hash
        hash_data = f"{now_date}{value_mission}{device}{device_status}"
        
        # Apply hash SHA-256 to concatenated data
        hash_result = hashlib.sha256(hash_data.encode()).hexdigest()
        return hash_result
    except Exception as e:
        print(f"An error occurred: {e}")
