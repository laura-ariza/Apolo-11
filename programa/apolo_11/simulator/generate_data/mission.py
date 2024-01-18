import random 



def generate_mission() -> str:
    
    #dictionary with key: name of completed missions and
    #value: abbreviation missions  
    opcion_mission: dict[str,str]= {
        "OrbitOne" : "ORBONE",
        "ColonyMoon" : "CLNM",
        "VacMars" : "TMRS",
        "GalaxyTwo" : "GALXONE",
        "Unknown" : "UNKN"
        }
    
    # random dictionary values
    mission: str = random.choice(list(opcion_mission.values()))
    
    for item, value in opcion_mission.items():
        if value == mission: 
            value_mission = item
            
    return mission, value_mission

