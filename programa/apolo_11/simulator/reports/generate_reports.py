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
    
    for root, _, files in os.walk(directory):
        # Usar la ruta relativa como nombre del subfolder
        subfolder_name = os.path.relpath(root, directory)
        # Procesar los archivos solo si están en subfolders
        if subfolder_name != '.':
            summary_data = []
            device_counts = {}

            for filename in files:
                if filename.endswith(".log"):
                    file_path = os.path.join(root, filename)
                    file_data = extract_all_keys(file_path)
                    if file_data is not None:
                        summary_data.append(file_data)

                        # Contar los devices por misión y estado
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

            # Alamacenar el resumen de datos, devices y conteos por subfolder
            subfolder_reports[subfolder_name] = {"summary": summary_data, "device_counts": device_counts}

    return subfolder_reports


def create_reports(subfolder_reports):
    for subfolder_name, data in subfolder_reports.items():
        summary_data = data["summary"]
        device_counts = data["device_counts"]

        # Formato de acuerdo con los requerimientos de fecha y hora
        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Necesitamos sacar la parte de de subfolder_name para corregir formato, sin embargo, al hacerlo solo se crea el reporte para el primer subfolder
        report_file_name = f'APLSTATS-REPORTE-{subfolder_name}-{current_datetime}.log'
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
                    report.write(f"    {device}: {info['count']}\n")
                    for status, count in info["statuses"].items():
                        report.write(f"      {status}: {count}\n")
                report.write("\n")

        print(f"Report file '{report_file_name}' created successfully.")


# Esta ruta se debe reemplazar con la ruta relativa "devices" para que funcione en otras máquinas
# directory_path = '/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/simulator/devices'
