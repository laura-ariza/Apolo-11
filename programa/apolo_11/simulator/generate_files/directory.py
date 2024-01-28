from tools import Tools
import os
class Directory:

    def __init__(self, name, name_path):  
            self.__name__= name
            dir_path = Tools.path_absolut()
            if name_path is None:
                self.__name_path__ = os.path.join(dir_path, name)
            else:
                self.__name_path__ = os.path.join(name_path, name)
            self.__state__ = False
            self.create_directory()
                
    @property
    def name_path(self):
        return self.__name_path__
    
    @property
    def state(self):
        return self.__state__
    
    # Create a directory and return the directory path
    def create_directory(self):
        if not os.path.isdir(self.__name_path__):
            try:
                os.mkdir(self.__name_path__)
                self.__state__ = True
            except:
                print("Could not create directory");
        else:
            self.__state__ = True
        
