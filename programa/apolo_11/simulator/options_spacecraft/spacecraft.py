from dataclasses import dataclass


@dataclass
class Draw:
    """Class that allows data storage without the need to implement complex logic,
    in this case the "name" and "slogan" attributes are used that will be used
    when starting the program
    """
    name: str
    slogan: str

    def draw_spacecraft():
        """Shows the information of a ship in the console, it is implemented in classes
        that are inherited
        """
        print("No implementation")
