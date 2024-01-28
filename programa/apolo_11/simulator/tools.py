from os import path
import yaml
import json


class Tools(object):
    dict_content = {}
    dict_directories = {}
    count_executed: int = 1
    state = True

    @staticmethod
    def path_absolut():
        return path.dirname(__file__)

    @staticmethod
    def read_yaml() -> dict:
        content: dict = None
        dir_path = path.join(Tools.path_absolut(), 'config')
        file_path = path.join(dir_path, 'config.yaml')
        try:
            with open(file_path) as file_config:
                content = yaml.load(file_config, Loader=yaml.SafeLoader)
                Tools.dict_content = content
        except Exception as ex:
            print(ex)
            content = None
        return content

    @staticmethod
    def json_reports(full_dic_report):
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
