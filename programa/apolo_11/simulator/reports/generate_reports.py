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
    subfolder_reports = {}

    for root, _, files in os.walk(directory):
        # Use the relative path as the subfolder name
        subfolder_name = os.path.relpath(root, directory)

        # Process files only if they are in subdirectories
        if subfolder_name != '.':
            summary_data = []
            for filename in files:
                if filename.endswith(".log"):
                    file_path = os.path.join(root, filename)
                    file_data = extract_all_keys(file_path)
                    if file_data is not None:
                        summary_data.append(file_data)

            # Store the summary data for each subfolder
            subfolder_reports[subfolder_name] = summary_data

    return subfolder_reports

def create_reports(subfolder_reports):
    for subfolder_name, summary_data in subfolder_reports.items():
        report_file_name = f'report_{subfolder_name}.txt'
        with open(report_file_name, 'w') as report:
            for idx, info in enumerate(summary_data, start=1):
                report.write(f"File {idx} Summary:\n")
                for key, value in info.items():
                    report.write(f"  {key}: {value}\n")
                report.write("\n")
        print(f"Report file '{report_file_name}' created successfully.")

# Replace 'your_directory_path' with the path to the directory containing your JSON files
directory_path = '/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/simulator/devices'
subfolder_reports = process_files(directory_path)
create_reports(subfolder_reports)
