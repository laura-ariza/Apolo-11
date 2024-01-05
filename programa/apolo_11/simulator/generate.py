from generate_data.date import gen_date 
from generate_data.device_status import generate_device_status 
from generate_data.device import generate_device
from generate_data.mission import generate_mission 
from generate_data.hash import generate_hash
import random
import yaml
import os

def generate_data(dir_path):

    mission, value_mission = generate_mission()
    unkn: str = "UNKN"
    hash: str = "unknown"
    
    if mission == unkn:
        now_date = gen_date()
        device: str = "unknown"
        device_status: str = "unknown"
        
    else: 
        now_date = gen_date()
        device: str = generate_device()
        device_status: str = generate_device_status()
        hash = generate_hash(now_date, value_mission, device, device_status)

    files = f"APL{mission}-0000{random.randint(1, 1000)}.yaml"
    full_path = os.path.join(dir_path, files)
    
    '''
    with open(files, 'w') as file:
        file.write(f"Date: {now_date}\n")
        file.write(f"Mission: {value_mission}\n")
        file.write(f"Device: {device}\n")
        file.write(f"Device status: {device_status}\n")
        file.write(f"Hash: {hash}\n")
    '''
    
    with open(full_path, 'w') as file:
        data = {
            'Date': now_date,
            'Mission': value_mission,
            'Device': device,
            'Device Status': device_status,
            'Hash': hash
        }
        yaml.dump(data, file)       
        
def files_create(dir_path):
    min: int = 1 
    max: int = 3
    number_files: int = random.randint(min, max)

    for i in range(number_files):
        generate_data(dir_path)
    return    