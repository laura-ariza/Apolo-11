from generate_data.date import generate_date 
from generate_data.device_status import generate_device_status 
from generate_data.device import generate_device
from generate_data.mission import generate_mission 
from datetime import datetime
import random
#https://docs.python.org/es/3/library/hashlib.html
#Hashlib:this module implements a common interface to many different secure hash and message digest algorithms.
import hashlib
import yaml

def generate_data():

    mission, value_mission = generate_mission()
    unkn: str = "UNKN"
    
    if mission == unkn:
        now_date: datetime = generate_date()
        device: str = "unknown"
        device_status: str = "unknown"
        
    else: 
        now_date: datetime = generate_date()
        device: str = generate_device()
        device_status: str = generate_device_status()
        #concatenate relevant data to generate the hash
        hash_data = f"{now_date}{value_mission}{device}{device_status}"
        #apply hash SHA-256 to concatenated data
        hash_value = hashlib.sha256(hash_data.encode()).hexdigest()

    #files = f"APL{mission}-0000{random.randint(1, 1000)}.log"
    files = f"APL{mission}-0000{random.randint(1, 1000)}.yaml"
    
    '''
    with open(files, 'w') as file:
        file.write(f"Date: {now_date}\n")
        file.write(f"Mission: {value_mission}\n")
        file.write(f"Device: {device}\n")
        file.write(f"Device status: {device_status}\n")
        file.write(f"Hash: {hash}\n")
    '''
    
    with open(files, 'w') as file:
        data = {
            'Date': now_date,
            'Mission': value_mission,
            'Device': device,
            'Device Status': device_status,
            'Hash': hash_value
        }
        yaml.dump(data, file)        
        

min: int = 1 
max: int = 3
number_files: int = random.randint(min, max)

for i in range(number_files):
    generate_data()
    