generate_reports.py

This Python file is a utility for generating reports from JSON log files stored in a directory structure.

Here's a breakdown of its functionality:

1. extract_all_keys() Function: This function reads a JSON file and attempts to extract its contents. If successful, it returns the data as a dictionary; otherwise, it prints an error message and returns None.

2. process_files() Function: This function traverses through a directory, locating JSON log files. For each file found, it extracts data using the extract_all_keys() function. It then aggregates this data into summary statistics based on missions, devices, and their statuses. The results are organized into a dictionary containing subfolder-wise reports.

3. create_reports() Function: This function takes the processed data from process_files() and generates reports. It creates a report file for each subfolder within a designated directory. These reports contain detailed analyses of events, including mission-specific summaries, device counts, and status breakdowns. Additionally, it moves the simulation folders to a specified destination directory after creating the reports.

Overall, this script automates the generation of detailed reports from JSON log files, providing valuable insights into events, missions, and device statuses within a given directory structure.






