
import os
import json

def extract_all_keys(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {file_path}: {e}")
            return None

def process_files(directory):
    extracted_info = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".log") or filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                file_data = extract_all_keys(file_path)
                if file_data is not None:
                    extracted_info.append(file_data)
    return extracted_info

# Replace 'your_directory_path' with the path to the directory containing your JSON files
directory_path = '/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/simulator/devices'
result = process_files(directory_path)

# Print the extracted information
for idx, info in enumerate(result, start=1):
    print(f"File {idx}:\n{info}")