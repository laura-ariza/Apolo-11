from typing import List, Union
from dataframe_dashboard import DataFrame
from tabulate import tabulate
import pandas as pd
from tools import Tools

class DashboardApolo11():
    def __init__(self, json_path: str):
        """
        Initialize the DashboardApolo11 with a DataFrame from a JSON file.

        Parameters:
        - json_path (str): The path to the JSON file.

        Returns:
        - None
        """
        # Use class method
        self.data: pd.DataFrame = DataFrame.json(json_path)
        
        # Get column names
        self.columns: List[str] = self.data.columns.tolist()

        # Change date format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format = Tools.dict_content['date_format'])

    def calculate_percentage(self, columns: List[str]) -> None:
        """
        Calculate and print the percentage and number of reports for each column in the DataFrame.

        Parameters:
        - columns (List[str]): The list of columns for which to calculate percentages.

        Returns:
        - None
        """
        for c in columns:
            print(f"\n********************  Percentage and Number of Reports by {c} ******************** \n")
            # Calculate percentage
            percentage = (self.data[c].value_counts() / self.data[c].value_counts().sum()) * 100

            # Calculate count
            count = self.data[c].value_counts()

            # Format the percentage with two decimals
            format_percentage = percentage.map("{:.2f} %".format)

            # Create a DataFrame for the format
            df_percentage = pd.DataFrame({'Percentage': format_percentage, 'Count': count})

            result = tabulate(df_percentage, headers=[c, 'Percentage', '# Reports'], tablefmt='pretty')

            # Print the result
            print(result)

    def missions_by_simulation(self) -> None:
        """
        Print the number of missions by simulation.

        Returns:
        - None
        """
        # Filter relevant columns
        filter_df = self.data[['Mission', 'Simulation']]

        # Count the number of missions by simulation
        mission_counts = filter_df.groupby(['Simulation', 'Mission']).size().unstack(fill_value=0)

        # Create DataFrame
        df_mission = pd.DataFrame(mission_counts)

        # Get column names
        columns: List[str] = df_mission.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Simulation'] + columns

        # Print the result
        print("\n********************  Number of Missions by Simulation  ******************** \n")
        print(tabulate(df_mission, headers=header, tablefmt='pretty'))

    def device_by_mission(self) -> None:
        """
        Print the number of devices by mission.

        Returns:
        - None
        """
        # Filter relevant columns
        filter = self.data[['Mission', 'Device']]

        # Count the number of devices by mission
        device_counts = filter.groupby(['Mission', 'Device']).size().unstack(fill_value=0)

        # Create DataFrame
        df_device = pd.DataFrame(device_counts)

        # Get column names
        columns: List[str] = df_device.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Mission'] + columns

        # Print the result
        print("\n********************  Number of Device by Mission  ******************** \n")
        print(tabulate(df_device, headers=header, tablefmt='pretty'))

    def device_status_by_device(self) -> None:
        """
        Print the number of device statuses by device.

        Returns:
        - None
        """
        # Filter relevant columns
        filter = self.data[['Device', 'Device Status']]

        # Count the number of device statuses by device
        device_status_counts = filter.groupby(['Device', 'Device Status']).size().unstack(fill_value=0)
        
        # Create DataFrame
        df_device_status = pd.DataFrame(device_status_counts)

        # Get column names
        columns: List[str] = df_device_status.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Device'] + columns

        # Print the result
        print("\n********************  Number of Device Status by Device  ******************** \n")
        print(tabulate(df_device_status, headers=header, tablefmt='pretty'))

