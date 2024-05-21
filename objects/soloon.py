from .astral_object import AstralObject

class Soloon(AstralObject):
    def __init__(self, row, column, api_client, color):
        super().__init__(row, column, api_client)
        self.color = color

    @property
    def endpoint(self):
        return "/soloons"

    def additional_data(self):
        return {"color": self.color}
