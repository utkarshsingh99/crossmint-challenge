from .polyanet import Polyanet
from .cometh import Cometh
from .soloon import Soloon

class AstralObjectFactory:
    @staticmethod
    def create_astral_object(obj_type, row, column, api_client):
        if obj_type == "POLYANET":
            return Polyanet(row, column, api_client)
        elif "SOLOON" in obj_type:  # Handle different colored Moons (Soloons)
            color = obj_type.split('_')[0].lower()
            return Soloon(row, column, api_client, color)
        elif "COMETH" in obj_type:  # Handle different directed Comets
            direction = obj_type.split('_')[0].lower()
            return Cometh(row, column, api_client, direction)
        else:
            raise ValueError(f"Unknown astral object type: {obj_type}")
