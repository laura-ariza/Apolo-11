import os
import json
from datetime import datetime


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

    for root, dirs, files in os.walk(directory):
        # Use the relative path as the name of the subfolder
        subfolder_name = os.path.relpath(root, directory)

        # Process the files only if they are in subfolders (excluding the new level)
        if subfolder_name != '.' and subfolder_name.count(os.path.sep) == 1:
            summary_data = []
            device_counts = {}

            for filename in files:
                if filename.endswith(".log"):
                    file_path = os.path.join(root, filename)
                    file_data = extract_all_keys(file_path)
                    if file_data is not None:
                        summary_data.append(file_data)

                        # Count devices by mission and status
                        mission = file_data.get("Mission", "Unknown")
                        device = file_data.get("Device", "Unknown")
                        device_status = file_data.get("Device Status", "Unknown")

                        if mission not in device_counts:
                            device_counts[mission] = {}

                        if device not in device_counts[mission]:
                            device_counts[mission][device] = {"count": 0, "statuses": {}}

                        device_counts[mission][device]["count"] += 1

                        status_key = f"{device} Status: {device_status}"
                        device_counts[mission][device]["statuses"][status_key] = device_counts[mission][device]["statuses"].get(status_key, 0) + 1

            # Store the data summary, devices, and counts per subfolder
            subfolder_reports[subfolder_name] = {"summary": summary_data, "device_counts": device_counts}

    return subfolder_reports


def create_reports(subfolder_reports):
    for subfolder_name, data in subfolder_reports.items():
        summary_data = data["summary"]
        device_counts = data["device_counts"]

        # Format according to date and time requirements
        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Include only the simulation level in the report file name
        subfolder_parts = subfolder_name.split(os.path.sep)
        simulation_name_for_folder = subfolder_parts[-2]  # Take only the simulation level

        # Create a subfolder for each simulation within the reports folder
        simulation_folder = os.path.join("reports", simulation_name_for_folder)
        os.makedirs(simulation_folder, exist_ok=True)

        # Include both simulation and execution levels in the report file name
        execution_name_for_file = subfolder_parts[-1]
        report_file_name = os.path.join(simulation_folder, f'APLSTATS-REPORTE-{execution_name_for_file}-{current_datetime}.log')

        with open(report_file_name, 'w') as report:
            report.write("Summary:\n")
            for idx, info in enumerate(summary_data, start=1):
                report.write(f"  File {idx} Summary:\n")
                for key, value in info.items():
                    report.write(f"    {key}: {value}\n")
                report.write("\n")
            
            report.write("\nDevice Counts:\n")
            for mission, devices in device_counts.items():
                report.write(f"  Mission: {mission}\n")
                for device, info in devices.items():
                    count_value = info["count"]
                    report.write(f"    {device}: {count_value}\n")
                    if "statuses" in info:
                        for status, count in info["statuses"].items():
                            report.write(f"      {device} Status: {status}: {count}\n")
                report.write("\n")
                
        print(f"Report file '{report_file_name}' created successfully.")


"""
This code creates a report by execution

def create_reports(subfolder_reports):
    for subfolder_name, data in subfolder_reports.items():
        summary_data = data["summary"]
        device_counts = data["device_counts"]

        # Format according to date and time requirements
        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Include both simulation and execution levels in the report file name
        subfolder_parts = subfolder_name.split(os.path.sep)
        simulation_name_for_file = subfolder_parts[-2]
        execution_name_for_file = subfolder_parts[-1]
        report_file_name = os.path.join("reports", f'APLSTATS-REPORTE-{simulation_name_for_file}-{execution_name_for_file}-{current_datetime}.log')

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(report_file_name), exist_ok=True)

        with open(report_file_name, 'w') as report:
            report.write("Summary:\n")
            for idx, info in enumerate(summary_data, start=1):
                report.write(f"  File {idx} Summary:\n")
                for key, value in info.items():
                    report.write(f"    {key}: {value}\n")
                report.write("\n")
            
            report.write("\nDevice Counts:\n")
            for mission, devices in device_counts.items():
                report.write(f"  Mission: {mission}\n")
                for device, info in devices.items():
                    count_value = info["count"]
                    report.write(f"    {device}: {count_value}\n")
                    if "statuses" in info:
                        for status, count in info["statuses"].items():
                            report.write(f"      {device} Status: {status}: {count}\n")
                report.write("\n")
                
        print(f"Report file '{report_file_name}' created successfully.")
"""

"""
This code creates a report per simulation
   def create_reports(subfolder_reports):
    for subfolder_name, data in subfolder_reports.items():
        summary_data = data["summary"]
        device_counts = data["device_counts"]

        # Format according to date and time requirements
        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Include only the simulation level in the report file name
        subfolder_parts = subfolder_name.split(os.path.sep)
        simulation_name_for_file = subfolder_parts[-2]  # Take only the simulation level
        report_file_name = os.path.join("reports", f'APLSTATS-REPORTE-{simulation_name_for_file}-{current_datetime}.log')

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(report_file_name), exist_ok=True)

        with open(report_file_name, 'w') as report:
            report.write("Summary:\n")
            for idx, info in enumerate(summary_data, start=1):
                report.write(f"  File {idx} Summary:\n")
                for key, value in info.items():
                    report.write(f"    {key}: {value}\n")
                report.write("\n")
            
            report.write("\nDevice Counts:\n")
            for mission, devices in device_counts.items():
                report.write(f"  Mission: {mission}\n")
                for device, info in devices.items():
                    count_value = info["count"]
                    report.write(f"    {device}: {count_value}\n")
                    if "statuses" in info:
                        for status, count in info["statuses"].items():
                            report.write(f"      {device} Status: {status}: {count}\n")
                report.write("\n")
                
        print(f"Report file '{report_file_name}' created successfully.") 
"""


# Esta ruta se debe reemplazar con la ruta relativa "devices" para que funcione en otras máquinas
# directory_path = '/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/simulator/devices'
