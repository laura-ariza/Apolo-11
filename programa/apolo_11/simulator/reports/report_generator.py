
import os
import json
print("Current working directory:", os.getcwd())

def extract_device_info(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            device_info = data.get('Mission')
            if device_info:
                return device_info
            else:
                print(f"No 'device' key found in {file_path}")
                return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {file_path}: {e}")
            return None

def process_files(directory):
    extracted_info = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".log") or filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                device_info = extract_device_info(file_path)
                if device_info is not None:
                    extracted_info.append(device_info)
    return extracted_info

# Replace 'your_directory_path' with the path to the directory containing your JSON files
directory_path = '/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/simulator/devices'
result = process_files(directory_path)

# Print the extracted information
for idx, info in enumerate(result, start=1):
    print(f"File {idx}: {info}")