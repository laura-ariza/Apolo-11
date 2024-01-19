'''
This is work in progress

import os
import yaml
import json

def collect_device_values():
    # Get the path of the current Python script
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # Create the folder path for YAML files in the same directory
    folder_path = os.path.join(script_folder, 'devices')

    device_values = []

    # Iterate through all files in the given folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a YAML file
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(file_path, 'r') as file:
                try:
                    # Load YAML content
                    yaml_content = yaml.safe_load(file)
                    
                    # Check if "device" key exists and add its value to the list
                    if 'device' in yaml_content:
                        device_values.append(yaml_content['device'])
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML file {filename}: {e}")

    return device_values

# Example usage
result = collect_device_values()
print("Collected device values:", result)
'''


