import time

def run_file(file_path):
    try:
        exec(open(file_path).read())
    except Exception as e:
        print(f"Error running file: {e}")

def main():
    # Specify the relative_path provided by the developer

    print("Press 'Ctrl+C' to stop the program.")
    
    file_path = "/Users/santiago.munoz/Documents/GitHub clone/Apolo-11/programa/apolo_11/path_test.py"
    
    while True:
        run_file(file_path)
        time.sleep(5)

if __name__ == "__main__":
    main()

