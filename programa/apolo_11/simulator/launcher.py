import time
import generate as gd
import os
from datetime import datetime


count_executed: int = 1


#create a directory and return the directory path
def new_dir():
    dir_name = "simulation_" + str(datetime.now()).replace(":", "_") #definir reglas de nombre de carpetas
    dir_devices = "devices"
    absolute_path = os.path.dirname(__file__)
    print("esto es lo que imprime: ", absolute_path)
    dir_path = ""
    dir_path = os.path.join(absolute_path, dir_devices)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    dir_path = os.path.join(dir_path, dir_name)
    os.mkdir(dir_path)
    print("este es el path" + dir_path)
    return dir_path

def dir_executed(dir_path):
    global count_executed
    new_dir_path = os.path.join(dir_path, f"executed_{count_executed}")
    count_executed += 1
    os.mkdir(new_dir_path)
    return new_dir_path

def run_file(file_path):
    try:
        exec(open(file_path).read())
    except Exception as e:
        print(f"Error running file: {e}")
        

def main():
    # Specify the relative_path provided by the developer

    print("Press 'Ctrl+C' to stop the program.")
    
    #file_path = "../apolo_11/path_test.py"
    dir_path_simulator = new_dir()
    while True:
        dir_path = dir_executed(dir_path_simulator)
        gd.files_create(dir_path)
        #run_file(file_path)
        time.sleep(5)
        

if __name__ == "__main__":
    main()
