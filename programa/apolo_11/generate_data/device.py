import random 

def generate_device() -> str:
    
    #list of device options 
    opcion_device: list[str] = ["satellites", "airplanes", "suits", "vehicles"]
    
    #device randomization
    device_type:str = random.choice(opcion_device)
    return device_type