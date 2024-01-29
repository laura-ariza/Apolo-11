from options_spacecraft.spacecraft import Draw


class SpacecraftDefault(Draw):
    """Class that inherits from the Draw object

    Args:
        Draw (object): Argument declared to inherit from Draw class
    """
    def __init__(self, name: str, slogan: str) -> None:
        """Class constructor

        Args:
            name (str): String that gets the name of the spacecraft
            slogan (str): String that gets the spaceship slogan
        """
        # Goes to the parent class and gets the attributes, way to access the constructor of the parent class
        super().__init__(name, slogan)

    def draw_spacecraft(self) -> None:
        """Print the spacecraft graph and its data via console
        """
        print(r"""
            |
           / \
          / _ \
         |.o '.|
         |'._.'|
         |     |
       ,'|  |  |`.
      /  |  |  |  \
      |,-'--|--'-.|
        """)
        print(self.name)
        print(self.slogan)
