import random


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
        self._mission_options: dict[str, str] = {
            "OrbitOne": "ORBONE",
            "ColonyMoon": "CLNM",
            "VacMars": "TMRS",
            "GalaxyTwo": "GALXONE",
            "Unknown": "UNKN"
        }

    def generate_mission(self) -> tuple[str, str]:
        """
        Generates a random mission and its corresponding value.

        Returns:
            Tuple[str, str]: Randomly selected mission and its value.
        """
        mission = random.choice(list(self._mission_options.values()))
        value_mission = [key for key, value in self._mission_options.items() if value == mission][0]
        return mission, value_mission

    def __str__(self) -> str:
        """
        Returns a string representation of Mission_Generator instance.

        Returns:
            str: String representation of Mission_Generator.
        """
        return f"Mission_Generator instance with options: {self._mission_options}"

