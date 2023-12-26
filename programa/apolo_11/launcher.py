import subprocess
import threading
import time

def run_file(file_path):
    try:
        subprocess.run(["python", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running file: {e}")

def listen_for_quit():
    global running
    input("Press 'Enter' to stop the program. \n")
    running = False

def main():
    global running
    running = True
    
    # Specify the file path provided by the developer
    # file_path = "/Users/santiago.munoz/Documents/Apolo-11/path_test.py"
    file_path = "/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/path_test.py"
    
    quit_thread = threading.Thread(target=listen_for_quit)
    quit_thread.start()

    while running:
        run_file(file_path)
        time.sleep(5)

    quit_thread.join()

if __name__ == "__main__":
    main()