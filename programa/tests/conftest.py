"""Configurations for testing"""

import pytest
from apolo_11.simulator.tools import Tools

@pytest.fixture(scope="session")
def app_instans():

    class App():
        pass
    
    app = App()
    
    app.path_absolut = Tools.path_absolut
    return app