from .astral_object import AstralObject

class Cometh(AstralObject):
    def __init__(self, row, column, api_client, direction):
        super().__init__(row, column, api_client)
        self.direction = direction

    @property
    def endpoint(self):
        return "/comeths"

    def additional_data(self):
        return {"direction": self.direction}
