from tools import Tools
from generate_data.date import generate_date
from generate_data.device_status import generate_device_status
from generate_data.device import generate_device
from generate_data.mission import Mission_Generator
from generate_data.hash import generate_hash
import random
import os
import json


class DataGenerator(): 
    @staticmethod
    def generate_data(dir_path):

        mission_generator: Mission_Generator = Mission_Generator()
        mission: str
        value_mission: str
        mission, value_mission = mission_generator.generate_mission()

        unkn: str = "UNKN"
        hash: str = "unknown"

        if mission == unkn:
            now_date: str = generate_date()
            device: str = "unknown"
            device_status: str = "unknown"
        else:
            now_date: str = generate_date()
            device: str = generate_device()
            device_status: str = generate_device_status()
            hash = generate_hash(now_date, value_mission, device, device_status)

        prefix = Tools.dict_content['details_name_files']['prefix']
        separator = Tools.dict_content['details_name_files']['separator']
        sequence_min = Tools.dict_content['details_name_files']['sequence_min']
        sequence_max = Tools.dict_content['details_name_files']['sequence_max']
        extension = Tools.dict_content['details_name_files']['extension']
        name_file = f"{prefix}{mission}{separator}{random.randint(sequence_min, sequence_max)}{extension}"
        full_path = os.path.join(dir_path, name_file)

        with open(full_path, 'w') as file:
            data = {
                'Date': now_date,
                'Mission': value_mission,
                'Device': device,
                'Device Status': device_status,
                'Hash': hash
            }
            json.dump(data, file, indent=4)

    @property
    def dir_path(self):
        return self.__dir_path__

    @staticmethod
    def files_creates(dir_path):
        min = Tools.dict_content['simulation_config']['count_file_min']
        max = Tools.dict_content['simulation_config']['count_file_max']
        number_files: int = random.randint(min, max)
        for i in range(number_files):
            DataGenerator.generate_data(dir_path)
        print(f"--> Generated files: {number_files}")
