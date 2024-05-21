from .astral_object import AstralObject

class Polyanet(AstralObject):
    @property
    def endpoint(self):
        return "/polyanets"

    def additional_data(self):
        return {}
