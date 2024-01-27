# local library
import generate as gd
import reports.generate_reports as generate_reports
from generate_files.directory import Directory
from tools import Tools

# python library
import time
from datetime import datetime
import threading


# Creación de directorios
def create_directory():
    # Creacion de directorios principales
    dir_files = Directory('files', None)
    dir_devices = Directory('devices', dir_files.name_path)
    dir_reports = Directory('reports', dir_files.name_path)
    dir_backups = Directory('backups', dir_files.name_path)

    # agregacion de directorios a diccionario de herramientas
    Tools.dict_directories['dir_files'] = dir_files
    Tools.dict_directories['dir_devices'] = dir_devices
    Tools.dict_directories['dir_reports'] = dir_reports
    Tools.dict_directories['dir_backups'] = dir_backups


# Initialize a thread in parallel to the simulation
def threading_simulation(dir_simulation):
    Tools.count_executed = 1
    while Tools.state:
        name_executed = f"execution_{Tools.count_executed}"
        Tools.count_executed += 1
        print(name_executed)
        dir_execute = Directory(name_executed, dir_simulation.name_path)
        # Genera los archivos
        time_seconds = Tools.dict_content['simulation_config']['time_seconds']
        gd.files_create(dir_execute.name_path)
        time.sleep(time_seconds)


def run_simulation():
    Tools.state = True
    dir_name_simulation: str = "simulation_" + str(datetime.now()).replace(":", "_")
    dir_simulation = Directory(dir_name_simulation, Tools.dict_directories['dir_devices'].name_path)

    print("Simulation in progress...")
    thread_simulation = threading.Thread(target=threading_simulation, args=(dir_simulation,))
    print('', 'Press Enter to stop the simulation and continue', sep="\n")
    thread_simulation.start()

    input()
    Tools.state = False
    print("ending simulation...")


def run_reports():
    print("Report generated  to path --> ", Tools.dict_directories['dir_devices'].name_path)
    subfolder_reports = generate_reports.process_files(
        Tools.dict_directories['dir_devices'].name_path)
    Tools.json_reports(subfolder_reports)
    generate_reports.create_reports(
        subfolder_reports,
        Tools.dict_directories['dir_reports'].name_path,
        Tools.dict_directories['dir_devices'].name_path,
        Tools.dict_directories['dir_backups'].name_path)


def run_dashboard():
    return


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

    print("¡Welcome to Apollo 11!", "1. Start a new simulation", "2. Generate reports", "3. Dashborad", "4. Salir", sep="\n")
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


def main():
    create_directory()
    # cargue de archivo de configuracion enlazado con diccionario de herramientas dict_content
    Tools.read_yaml()
    menu()


if __name__ == "__main__":
    main()
