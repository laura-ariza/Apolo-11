from tools import Tools
import os
class Directory:
    
    def __init__(self, name: str, name_path: str) -> None:
        """Constructor of the directory class which receives two arguments
        which contain the path information to the directory to be created

        Args:
            name (str): Name of the folder you want to create
            name_path (str): Path of the folder you want to create
        """
        self.__name__= name
        dir_path = Tools.path_absolut()
        if name_path is None:
            self.__name_path__ = os.path.join(dir_path, name)
        else:
            self.__name_path__ = os.path.join(name_path, name)
        self.__state__ = False
        self.create_directory()
                
    @property
    def name_path(self) -> str:
        """Brings the name of the path

        Returns:
            str: Returns the path used in the class
        """
        return self.__name_path__
    
    @property
    def state(self) -> bool:
        """Validates if the folder has already been created, if not, allows
        it to be created

        Returns:
            bool: Changes its state depending on the creation of the folder
        """
        return self.__state__
    
    def create_directory(self) -> None:
        """Allows the creation of a new folder
        """
        if not os.path.isdir(self.__name_path__):
            try:
                os.mkdir(self.__name_path__)
                self.__state__ = True
            except:
                print("Could not create directory");
        else:
            self.__state__ = True
        
