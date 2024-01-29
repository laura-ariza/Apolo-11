import pandas as pd
import json


class DataFrame():
    @classmethod
    def json(cls, json_file: str) -> pd.DataFrame:
        """
        Build a DataFrame from a JSON file.

        Parameters:
        - json_file (str): The path to the JSON file.

        Returns:
        - pd.DataFrame: The resulting DataFrame.
        """
        # Read JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        # Initializes an empty DataFrame
        df = pd.DataFrame()

        # Iterates over each simulation and adds the information as columns to the DataFrame
        for simulation, details in data.items():
            simulation_df = pd.DataFrame(details['summary'])
            simulation_df['Simulation'] = simulation
            df = pd.concat([df, simulation_df], ignore_index=True)

        return df
