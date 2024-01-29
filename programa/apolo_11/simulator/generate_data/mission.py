from tools import Tools

import random
import logging

logging.basicConfig(filename='mission.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Mission_Generator:
    """
    A class for generating missions and their corresponding values.

    Attributes:
        _mission_options (dict): A dictionary mapping mission names to their values.

    Methods:
        generate_mission() -> Tuple[str, str]: Generates a random mission and its value.
    """
    def __init__(self) -> None:
        """
        Initializes Mission_Generator with predefined mission options.
        """
        self._mission_options: dict[str, str] = Tools.dict_content['mission_options']

    def generate_mission(self) -> tuple[str, str]:
        """
        Generates a random mission and its corresponding value.

        Returns:
            Tuple[str, str]: Randomly selected mission and its value.
        """

        try:
            mission = random.choice(list(self._mission_options.values()))
            value_mission = [key for key, value in self._mission_options.items() if value == mission][0]
            logging.info("Mission generated successfully.")
            return mission, value_mission

        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def __str__(self) -> str:
        """
        Returns a string representation of Mission_Generator instance.

        Returns:
            str: String representation of Mission_Generator.
        """
        return f"Mission_Generator instance with options: {self._mission_options}"
