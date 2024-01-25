import time
import generate as gd
import reports.generate_reports as generate_reports
import os
from datetime import datetime


count_executed: int = 1


# def new_dir_simulation(dir_path):
#     dir_path = os.path.join(dir_path, dir_name)
#     if not os.path.isdir(dir_path):
#         os.mkdir(dir_path)
#     return dir_path

# Create a directory and return the directory path
def new_directory(name_directory:str, path_directory:str):
    if path_directory == "":
        path_directory = os.path.dirname(__file__)
    dir_path = os.path.join(path_directory, name_directory)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    return dir_path


def run_file(file_path):
    try:
        exec(open(file_path).read())
    except Exception as e:
        print(f"Error running file: {e}")


def main():
    global count_executed
    # Specify the relative_path provided by the developer
    dir_path_files = new_directory("files", "")
    dir_path_devices = new_directory("devices", dir_path_files)
    dir_name_simulation: str = "simulation_" + str(datetime.now()).replace(":", "_") # definir reglas de nombre de carpetas
    dir_path_simulation = new_directory(dir_name_simulation, dir_path_devices)
    dir_path_reports = new_directory("reports", dir_path_files)
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
       
    print("¡Welcome to Apollo 11!","1. Start a new simulation","2. Generate reports", sep="\n")
    option = input("Type an option:")
    if option == "1":
        print("Simulation in progress...", "Press 'Ctrl+C' to stop the simulation.", sep="\n")
        while True:
            name_executed = f"execution_{count_executed}"
            count_executed += 1
            dir_path = new_directory(name_executed, dir_path_simulation)
            gd.files_create(dir_path)
            time.sleep(5)
    elif option == "2":
        print("Report generated  to path --> ", dir_path_devices)
        subfolder_reports = generate_reports.process_files(dir_path_devices)
        generate_reports.create_reports(subfolder_reports, dir_path_reports)        

if __name__ == "__main__":
    main()
