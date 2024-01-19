import random 


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
        return device_status
    except Exception as e:
        print(f"An error occurred: {e}")
        