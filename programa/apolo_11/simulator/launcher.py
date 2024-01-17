import time
import generate as gd
import os
from datetime import datetime


# create a directory and return the directory path
def new_dir():
    dir_name = "dir_" + str(datetime.now()).replace(":", "_")  # definir reglas de nombre de carpetas
    dir_devices = "devices"
    absolute_path = os.path.dirname(__file__)
    dir_path = ""
    if not os.path.isdir(dir_devices):
        os.mkdir(dir_devices)
    dir_path = os.path.join(absolute_path, dir_devices)
    dir_path = os.path.join(dir_path, dir_name)
    os.mkdir(dir_path)
    print("este es el path" + dir_path)
    return dir_path


def run_file(file_path):
    try:
        exec(open(file_path).read())
    except Exception as e:
        print(f"Error running file: {e}")


def main():
    # Specify the relative_path provided by the developer
    print("Press 'Ctrl+C' to stop the program.")

    dir_path = new_dir()
    while True:
        gd.files_create(dir_path)
        time.sleep(5)


if __name__ == "__main__":
    main()
