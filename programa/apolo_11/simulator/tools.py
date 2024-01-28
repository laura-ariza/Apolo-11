from os import path
import yaml
import json
from typing import Dict


class Tools(object):
    """
    Static class that groups tools commonly used in the project, such as configuration data and routes.
    """
    dict_content = {}
    dict_directories = {}
    count_executed: int = 1
    state = True

    @staticmethod
    def path_absolut() -> str:
        return path.dirname(__file__)

    @staticmethod
    def read_yaml() -> None:
        """
        Reads the configuration file and loads it into the general purpose dictionary (dict_content)
        """
        dir_path = path.join(Tools.path_absolut(), 'config')
        file_path = path.join(dir_path, 'config.yaml')
        try:
            with open(file_path) as file_config:
                Tools.dict_content = yaml.load(file_config, Loader=yaml.SafeLoader)
        except Exception as ex:
            print(ex)

    @staticmethod
    def json_reports(full_dic_report: Dict[str, str]) -> None:
        """Adds or updates the dictionary information received by parameter in the "files" path and converts it to a file in .json format

        Args:
            full_dic_report (dict): Contains the information of the generated reports
        """
        temporal_dict = {}
        # json_string = json.dumps(full_dic_report)
        file_path = path.join(Tools.dict_directories['dir_files'].name_path, 'dashboard.json')
        # dir_path = os.path.join(os.path.dirname(__file__), 'dashboard.json')
        try:
            with open(file_path) as file:
                temporal_dict = json.load(file)
                temporal_dict.update(full_dic_report)
        except Exception as ex:
            print(ex)
            temporal_dict = {}
        temporal_dict.update(full_dic_report)
        with open(file_path, 'w') as write_file:
            json.dump(temporal_dict, write_file, indent=4)
