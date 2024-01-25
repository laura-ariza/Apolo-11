import yaml
import time
import generate as gd
import reports.generate_reports as generate_reports
import os
from datetime import datetime
import threading


count_executed: int = 1
state = True
path_apolo:dict = {}
dict_values_simulation:dict = {}


# Access the configuration file
def read_yaml(path:str) -> dict:
    content: dict = None
    dir_path = os.path.join(path, 'config')
    file_path = os.path.join(dir_path, 'config.yaml')
    try:
        with open(file_path) as file_config:
            content = yaml.load(file_config, Loader=yaml.SafeLoader)
    except Exception as ex:
        print(ex)
        content = None
    return content


# Create a directory and return the directory path
def new_directory(name_directory:str, path_directory:str):
    if path_directory == "":
        path_directory = os.path.dirname(__file__)
    dir_path = os.path.join(path_directory, name_directory)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    return dir_path


def create_content():
    # Specify the relative_path provided by the developer
    dir_path_files: str = new_directory("files", "")
    dir_path_devices: str = new_directory("devices", dir_path_files)
    dir_path_reports: str = new_directory("reports", dir_path_files)
    dir_path_backups: str = new_directory("backups", dir_path_files)
    path_apolo['dir_path_files'] = dir_path_files
    path_apolo['dir_path_devices'] = dir_path_devices
    path_apolo['dir_path_reports'] = dir_path_reports
    path_apolo['dir_path_backups'] = dir_path_backups

# Inicializa una hebra en paralelo a la simulacion
def threading_simulation(dir_path_simulation):
    global count_executed, path_apolo, dict_values_simulation
    while state:
        name_executed = f"execution_{count_executed}"
        count_executed += 1
        print(count_executed, name_executed)
        dir_path = new_directory(name_executed, dir_path_simulation)
        # Genera los archivos
        min = dict_values_simulation['simulation_config']['count_file_min']
        max = dict_values_simulation['simulation_config']['count_file_max']
        time_seconds = dict_values_simulation['simulation_config']['time_seconds']
        gd.files_create(dir_path, min, max)
        time.sleep(time_seconds)

def run_simulation():
    global path_apolo, state
    state = True
    dir_name_simulation: str = "simulation_" + str(datetime.now()).replace(":", "_")
    dir_path_simulation = new_directory(
        dir_name_simulation, 
        path_apolo['dir_path_devices'])
    print("Simulation in progress...")
    thread_simulation = threading.Thread(target = threading_simulation, args=(dir_path_simulation,))
    print('','Press enter to continue', sep="\n")
    thread_simulation.start()
    
    input()
    state = False
    print("ending simulation...")

def run_reports():
    global path_apolo
    print("Report generated  to path --> ", path_apolo['dir_path_devices'])
    subfolder_reports = generate_reports.process_files(path_apolo['dir_path_devices'])
    generate_reports.create_reports(
        subfolder_reports, 
        path_apolo['dir_path_reports'],
        path_apolo['dir_path_devices'], 
        path_apolo['dir_path_backups'])


def menu():
    # Creation of options menu to generate simulation or reports
    print(r"""
        |
       / \
      / _ \
     |.o '.|
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \
  |,-'--|--'-.|
    """)

    print("¡Welcome to Apollo 11!","1. Start a new simulation","2. Generate reports", "3. Salir", sep="\n")
    option = input("Type an option:")
    if option == "1":
        run_simulation()
    elif option == "2":
        run_reports()
    elif option == "3":
        return
    menu()

def main():
    global dict_values_simulation
    path_absolut = os.path.dirname(__file__)
    dict_values_simulation = read_yaml(path_absolut)
    create_content()
    menu()

if __name__ == "__main__":
    main()
