# local library
from generate import DataGenerator
import reports.generate_reports as generate_reports
from generate_files.directory import Directory
from dashboard.visualization_dashboard import DashboardApolo11
from tools import Tools
from options_spacecraft.spacecraft_default import SpacecraftDefault
from options_spacecraft.spacecraft_nasa import SpacecraftNasa
from options_spacecraft.spacecratf_rocket import SpacecraftRocket

# python library
import time
from datetime import datetime
import threading
from os import path
import argparse


def create_directory() -> None:
    """Function used to create the directories necessary for the simulation process,
    it also adds the directories to the dictionary created in the tools file
    """
    # Create parent directories
    dir_files = Directory('files', None)
    dir_devices = Directory('devices', dir_files.name_path)
    dir_reports = Directory('reports', dir_files.name_path)
    dir_backups = Directory('backups', dir_files.name_path)

    # Add from directories to dictionary tools
    Tools.dict_directories['dir_files'] = dir_files
    Tools.dict_directories['dir_devices'] = dir_devices
    Tools.dict_directories['dir_reports'] = dir_reports
    Tools.dict_directories['dir_backups'] = dir_backups


def threading_simulation(dir_simulation: Directory) -> None:
    """Initializes a simulation thread in parallel of the entire simulation process

    Args:
        dir_simulation (Directory): It is an object that contains the directory
        information of the current simulation
    """
    Tools.count_executed = 1
    while Tools.state:
        name_executed = f"execution_{Tools.count_executed}"
        Tools.count_executed += 1
        print(name_executed)
        dir_execute = Directory(name_executed, dir_simulation.name_path)
        # Genera los archivos
        time_seconds = Tools.dict_content['simulation_config']['time_seconds']
        DataGenerator.files_creates(dir_execute.name_path)
        time.sleep(time_seconds)


def run_simulation() -> None:
    """Start the simulation with the creation of directories where all the generated
    information will be stored.
    """
    Tools.state = True
    dir_name_simulation: str = "simulation_" + str(datetime.now()).replace(":", "_")
    dir_simulation = Directory(dir_name_simulation, Tools.dict_directories['dir_devices'].name_path)

    print("Simulation in progress...")
    thread_simulation = threading.Thread(target=threading_simulation, args=(dir_simulation,))
    print('', 'Press Enter to stop the simulation and continue', sep="\n")
    thread_simulation.start()

    input()
    Tools.state = False
    print("Ending simulation...")


def run_reports() -> None:
    """Starts the generation of reports with the previously created files and saves
    them in a defined directory, also moving the processed information to the backups
    directory and creates the dashboard.json file
    """
    print("Report generated  to path --> ", Tools.dict_directories['dir_devices'].name_path)
    subfolder_reports = generate_reports.process_files(
        Tools.dict_directories['dir_devices'].name_path)
    file_path = path.join(Tools.dict_directories['dir_files'].name_path, 'dashboard.json')
    Tools.write_json_reports(subfolder_reports, file_path)
    generate_reports.create_reports(
        subfolder_reports,
        Tools.dict_directories['dir_reports'].name_path,
        Tools.dict_directories['dir_devices'].name_path,
        Tools.dict_directories['dir_backups'].name_path)


def run_dashboard() -> None:
    """Generates a summary of the files generated in the reports, based on the dashboard.json file
    """
    path_json_dashboard = path.join(Tools.dict_directories['dir_files'].name_path, 'dashboard.json')
    dashboard_apolo_11 = DashboardApolo11(path_json_dashboard)
    dashboard_apolo_11.calculate_percentage()
    dashboard_apolo_11.missions_by_simulation()
    dashboard_apolo_11.device_by_mission()
    dashboard_apolo_11.device_status_by_device()


def menu():
    """Functionality used to generate a menu of options with which the user can interact
    in the program according to what they want to process"""
    print("¡Welcome to Apollo 11!",
          "1. Start a new simulation",
          "2. Generate reports",
          "3. Dashborad",
          "4. Exit",
          sep="\n")
    option = input("Type an option:")
    if option == "1":
        run_simulation()
    elif option == "2":
        run_reports()
    elif option == "3":
        run_dashboard()
    elif option == "4":
        return
    menu()


def information_program() -> None:
    """It is a command line argument parser, it allows better interaction
    with the users when executing the program
    """
    parse = argparse.ArgumentParser(
        prog='Apollo 11',
        description="Simulator to missions",
        epilog="To infinity and beyond!!!"
    )
    parse.add_argument('-v', '--version', help='show version to simulator', required=False)
    parse.add_argument('-nasa', help='change init simulation', required=False)
    parse.add_argument('-rocket', help='change init simulation', required=False)
    args = parse.parse_args()
    if args.version:
        print("Simulator to version 1.0.0")
        return
    elif args.nasa:
        nv_nasa = SpacecraftNasa(
            Tools.dict_content['spacecraft_options']['name_nasa'],
            Tools.dict_content['spacecraft_options']['slogan_nasa'])
        nv_nasa.draw_spacecraft()
    elif args.rocket:
        nv_rocket = SpacecraftRocket(
            Tools.dict_content['spacecraft_options']['name_rocket'],
            Tools.dict_content['spacecraft_options']['slogan_rocket'])
        nv_rocket.draw_spacecraft()
    else:
        nv_default = SpacecraftDefault(
            Tools.dict_content['spacecraft_options']['name_default'],
            Tools.dict_content['spacecraft_options']['slogan_default'])
        nv_default.draw_spacecraft()


def main():
    """Main method of the program.
    This preloads the settings and prints the simulation menu
    """
    # load configuration file linked with dict_content tool dictionary
    dir_path = path.join(Tools.path_absolut(), 'config', 'config.yaml')
    Tools.dict_content = Tools.read_yaml(dir_path)

    information_program()
    create_directory()
    menu()


if __name__ == "__main__":
    main()
