from typing import List, Union
from dashboard.dataframe_dashboard import DataFrame
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
        self.data['Date'] = pd.to_datetime(self.data['Date'], format=Tools.dict_content['date_format'])

    def calculate_percentage(self) -> None:
        """
        Calculate and print the percentage and number of reports for each column in the DataFrame.

        This method iterates through each column in the DataFrame and calculates the percentage
        along with the number of reports. For the 'Hash' column, it performs additional calculations
        for 'unknown' and 'others' categories.

        Parameters:
        - columns (List[str]): The list of columns for which to calculate percentages.

        Returns:
        - None
        """
        
        for c in self.columns:
            print(f"\n********************  Percentage and Number of Reports by {c} ******************** \n")
            
            # Check if the current column is 'Hash'
            if c == 'Hash':
                # Calculate the percentage
                percentage_series: pd.Series = self.data[c].value_counts() / self.data[c].value_counts().sum() * 100
                hash_names: pd.Series = self.data[c]
                Total_hash: int = self.data[c].value_counts().sum()

                # Calculate the sum for 'unknown' and 'others'
                sum_unk: int = self.data.loc[self.data[c] == 'unknown', c].value_counts().sum()
                sum_others: int = self.data.loc[self.data[c] != 'unknown', c].value_counts().sum()

                # Calculate the percentages
                percentage_sum: float = (sum_unk / Total_hash) * 100
                percentage_others: float = (sum_others / Total_hash) * 100

                # Create a DataFrame for tabular presentation
                df_result: pd.DataFrame = pd.DataFrame({
                    c: ['unknown', 'others'],
                    'Percentage': [f'{percentage_sum:.2f}%', f'{percentage_others:.2f}%'],
                    '# Reports': [sum_unk, sum_others]
                })

                # Print the formatted table without indices
                result_table: str = tabulate(df_result, headers=[c, 'Percentage', '# Reports'], tablefmt='pretty', showindex=False)
                print(result_table)
            else:
                # Calculate percentage for non-'Hash' columns
                percentage: pd.Series = (self.data[c].value_counts() / self.data[c].value_counts().sum()) * 100

                # Calculate count
                count: pd.Series = self.data[c].value_counts()

                # Format the percentage with two decimals
                format_percentage: pd.Series = percentage.map("{:.2f} %".format)

                # Create a DataFrame for the format
                df_percentage: pd.DataFrame = pd.DataFrame({'Percentage': format_percentage, 'Count': count})

                result: str = tabulate(df_percentage, headers=[c, 'Percentage', '# Reports'], tablefmt='pretty')

                # Print the result
                print(result)

    def missions_by_simulation(self) -> None:
        """
        Print the percentage of missions by simulation.

        Returns:
        - None
        """
        # Filter relevant columns
        filter_df = self.data[['Mission', 'Simulation']]

        # Count the number of missions by simulation
        mission_counts = filter_df.groupby(['Simulation', 'Mission']).size().unstack(fill_value=0)

        # Calculate the percentage
        mission_percentage = mission_counts.div(mission_counts.sum(axis=1), axis=0) * 100
        
        # Format the percentage with two decimals
        format_percentage: pd.Series = mission_percentage.map("{:.2f} %".format)

        # Create DataFrame with percentages
        df_percentage = pd.DataFrame(format_percentage)

        # Get column names
        columns: List[str] = df_percentage.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Simulation'] + columns

        # Print the result
        print("\n********************  Percentage of Missions by Simulation  ******************** \n")
        print(tabulate(df_percentage, headers=header, tablefmt='pretty'))


    def device_by_mission(self) -> None:
        """
        Print the percentage of devices by mission.

        Returns:
        - None
        """
        # Filter relevant columns
        filter = self.data[['Mission', 'Device']]

        # Count the number of devices by mission
        device_counts = filter.groupby(['Mission', 'Device']).size().unstack(fill_value=0)
        
        # Calculate the percentage
        device_percentage = device_counts.div(device_counts.sum(axis=1), axis=0) * 100
        
        # Format the percentage with two decimals
        format_percentage: pd.Series = device_percentage.map("{:.2f} %".format)

        # Create DataFrame with percentages
        df_device = pd.DataFrame(format_percentage)

        # Get column names
        columns: List[str] = df_device.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Mission'] + columns

        # Print the result
        print("\n********************  Percentage of Device by Mission  ******************** \n")
        print(tabulate(df_device, headers=header, tablefmt='pretty'))

    def device_status_by_device(self) -> None:
        """
        Print the percentage of device statuses by device.

        Returns:
        - None
        """
        # Filter relevant columns
        filter = self.data[['Device', 'Device Status']]

        # Count the number of device statuses by device
        device_status_counts = filter.groupby(['Device', 'Device Status']).size().unstack(fill_value=0)

        # Calculate the percentage
        device_status_percentage = device_status_counts.div(device_status_counts.sum(axis=1), axis=0) * 100
        
        # Format the percentage with two decimals
        format_percentage: pd.Series = device_status_percentage.map("{:.2f} %".format)

        # Create DataFrame with percentages
        df_device_status = pd.DataFrame(format_percentage)

        # Get column names
        columns: List[str] = df_device_status.columns.tolist()

        # Column list
        header: List[Union[str, List[str]]] = ['Device'] + columns

        # Print the result
        print("\n********************  Percentage of Device Status by Device  ******************** \n")
        print(tabulate(df_device_status, headers=header, tablefmt='pretty'))
