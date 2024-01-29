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
    def read_yaml(file_path: str) -> Dict[str, str]:
        """Reads the configuration file and loads it into the general purpose dictionary (dict_content)

        Args:
            file_path (str): Receives the path of the .yaml file

        Returns:
            Dict[str, str]: Returns a dictionary with the contents of the .yaml file
        """
        content: dict = {}
        try:
            with open(file_path) as file_config:
                content = yaml.load(file_config, Loader=yaml.SafeLoader)
        except Exception as ex:
            print(ex)
        return content

    @staticmethod
    def write_json_reports(full_dic_report: Dict[str, str], file_path: str) -> None:
        """Adds or updates the dictionary information received by parameter in the "files"
        path and converts it to a file in .json format

        Args:
            full_dic_report (dict): Contains the information of the generated reports
            file_path (str): .json file path
        """
        temporal_dict = {}
        try:
            with open(file_path) as file:
                temporal_dict = json.load(file)
                temporal_dict.update(full_dic_report)
        except Exception:
            temporal_dict = {}
        temporal_dict.update(full_dic_report)
        with open(file_path, 'w') as write_file:
            json.dump(temporal_dict, write_file, indent=4)
