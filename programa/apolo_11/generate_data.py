from generate_data.date import generate_date 
from generate_data.device_status import generate_device_status 
from generate_data.device import generate_device
from generate_data.mission import generate_mission 
from generate_data.hash import generate_hash
import random


def generate_data():

    mission, value_mission = generate_mission()
    unkn: str = "UNKN"
    
    if mission == unkn:
        now_date = generate_date()
        device: str = "unknown"
        device_status: str = "unknown"
        
    else: 
        now_date = generate_date()
        device: str = generate_device()
        device_status: str = generate_device_status()
        hash = generate_hash(now_date, value_mission, device, device_status)

    files = f"APL{mission}-0000{random.randint(1, 1000)}.log"
    
    with open(files, 'w') as file:
        file.write(f"Date: {now_date}\n")
        file.write(f"Mission: {value_mission}\n")
        file.write(f"Device: {device}\n")
        file.write(f"Device status: {device_status}\n")
        file.write(f"Hash: {hash}\n")

min: int = 1 
max: int = 3
number_files: int = random.randint(min, max)

for i in range(number_files):
    generate_data()
    