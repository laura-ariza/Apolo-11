import random 

def generate_device() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    try:
        # List of device options 
        option_device: list[str] = ["satellites", "airplanes", "suits", "vehicles"]
        
        # Device randomization
        device_type: str = random.choice(option_device)
        return device_type
    except Exception as e:
        print(f"An error occurred: {e}")