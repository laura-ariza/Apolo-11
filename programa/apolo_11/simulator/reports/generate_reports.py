import logging
from tools import Tools
import os
import json
from datetime import datetime
import shutil

# Logging settings
logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


def extract_all_keys(file_path):
    """Extract all keys from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing the keys and values from the JSON file.
            Returns None if there is an error decoding JSON.

    """
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON in {file_path}: {e}")
            return None


def process_files(directory):
    """Process log files in a directory and generate a summary.

    Args:
        directory (str): The directory containing log files.

    Returns:
        dict: A dictionary containing the summary data, device counts, and subfolder names.

    """
    subfolder_reports = {}
    count_reports = 0
    for root, dirs, files in os.walk(directory):
        # Use the relative path as the name of the subfolder
        subfolder_name = os.path.relpath(root, directory)

        # Process the files only if they are in subfolders (excluding the new level)
        if subfolder_name != '.' and subfolder_name.count(os.path.sep) == 1:
            count_reports += 1
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
                        dev_count = device_counts[mission][device]["statuses"].get(status_key, 0) + 1
                        device_counts[mission][device]["statuses"][status_key] = dev_count

            # Store the data summary, devices, and counts per subfolder
            subfolder_reports[subfolder_name] = {"summary": summary_data, "device_counts": device_counts}
    if count_reports == 0:
        logging.warning(Tools.dict_content['control_errors']['no_found_reports'])

    return subfolder_reports


def create_reports(subfolder_reports, dir_path_reports, path_origin_directory: str, path_destination_directory: str):
    """
    Creates reports from the processed data.

    Args:
        subfolder_reports (dict): A dictionary containing subfolder-wise reports.
        dir_path_reports (str): The path to the directory to store the reports.
        path_origin_directory (str): The path to the original directory.
        path_destination_directory (str): The path to the destination directory.

    Returns:
        None
    """
    value_folder = ""
    for subfolder_name, data in subfolder_reports.items():
        # summary_data = data["summary"]
        device_counts = data["device_counts"]

        # Format according to date and time requirements
        current_datetime = datetime.now().strftime("%d-%m-%Y %H_%M_%S")

        # Include only the simulation level in the report file name
        subfolder_parts = subfolder_name.split(os.path.sep)
        simulation_name_for_folder = subfolder_parts[-2]  # Take only the simulation level

        # Create a subfolder for each simulation within the reports folder
        simulation_folder = os.path.join(dir_path_reports, simulation_name_for_folder)
        os.makedirs(simulation_folder, exist_ok=True)

        # Include both simulation and execution levels in the report file name
        execution_name_for_file = subfolder_parts[-1]
        report_file_name = os.path.join(
            simulation_folder,
            f'APLSTATS-REPORTE-{execution_name_for_file}-{current_datetime}.log')
        logging.info(f"Creating report file '{report_file_name}'...")
        with open(report_file_name, 'w') as report:
            report.write("\n********** EVENT ANALYSIS: **********\n")

            # Dictionary to store counts of faulty devices for each mission
            faulty_devices_summary = {}

            unknown_devices_summary = {}

            for mission, devices in device_counts.items():
                report.write(f"  Mission: {mission}\n")
                total_devices_count = sum(info["count"] for info in devices.values())
                faulty_status_count = 0  # Initialize count for "faulty" status devices
                unknown_status_count = 0
                for device, info in devices.items():
                    count_value = info["count"]
                    percentage = (count_value / total_devices_count) * 100 if total_devices_count > 0 else 0
                    report.write(f"    {device}: {count_value} ({percentage:.2f}%)\n")
                    if "statuses" in info:
                        for status, count in info["statuses"].items():
                            percentage_status = (count / count_value) * 100 if count_value > 0 else 0
                            report.write(f"     {status}: {count} ({percentage_status:.2f}%)\n")
                            if "faulty" in status.lower():
                                faulty_status_count += count
                            if "unknown" in status.lower():
                                unknown_status_count += count

                # Store the count of "faulty" status devices in the summary dictionary
                faulty_devices_summary[mission] = {
                    'count': faulty_status_count,
                    'percentage': (faulty_status_count / total_devices_count) * 100 if total_devices_count > 0 else 0
                }

                unknown_devices_summary[mission] = {
                    'count': unknown_status_count,
                    'percentage': (unknown_status_count / total_devices_count) * 100 if total_devices_count > 0 else 0
                }

                report.write("\n")

            # Include the section for device statuses and occurrences grouped by device
            report.write("\n********** SUMMARY OF DEVICE STATUSES BY DEVICE: **********\n")
            device_status_summary = {}

            for mission, devices in device_counts.items():
                for device, info in devices.items():
                    if "statuses" in info:
                        for status, count in info["statuses"].items():
                            if device not in device_status_summary:
                                device_status_summary[device] = {}
                            device_status_summary[device][status] = device_status_summary[device].get(status, 0) + count

            for device, statuses in device_status_summary.items():
                report.write(f"  Device: {device}\n")
                total_device_count = sum(statuses.values())
                for status, count in statuses.items():
                    percentage_status = (count / total_device_count) * 100 if total_device_count > 0 else 0
                    report.write(f"    {status}: {count} ({percentage_status:.2f}%)\n")

            # Include the summary section for faulty devices at the end of the report
            report.write("\n********** SUMMARY OF FAULTY DEVICES BY MISSION: **********\n")
            for mission, info in faulty_devices_summary.items():
                report.write(f"  {mission}: {info['count']} occurrences ({info['percentage']:.2f}%)\n")

            logging.info(f"Report file '{report_file_name}' created successfully.")
        # Validación de movimiento de carpeta de simulación
        if value_folder == "":
            value_folder = simulation_name_for_folder
        if value_folder != simulation_name_for_folder:
            dir_path_simulator = os.path.join(path_origin_directory, value_folder)
            shutil.move(dir_path_simulator, path_destination_directory)
            logging.info(f"Moved simulation folder '{value_folder}' to '{path_destination_directory}'.")
            value_folder = simulation_name_for_folder
    if value_folder != "":
        dir_path_simulator = os.path.join(path_origin_directory, value_folder)
        shutil.move(dir_path_simulator, path_destination_directory)
        logging.info(f"Moved simulation folder '{value_folder}' to '{path_destination_directory}'.")
