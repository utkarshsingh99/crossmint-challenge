from abc import ABC, abstractmethod

class AstralObject(ABC):
    def __init__(self, row, column, api_client):
        self.row = row
        self.column = column
        self.api_client = api_client

    @property
    @abstractmethod
    def endpoint(self):
        pass

    @abstractmethod
    def additional_data(self):
        pass

    def create(self):
        data = {
            "candidateId": self.api_client.candidate_id,
            "row": self.row,
            "column": self.column
        }
        data.update(self.additional_data())
        return self.api_client.post(self.endpoint, data)

    def delete(self):
        data = {
            "candidateId": self.api_client.candidate_id,
            "row": self.row,
            "column": self.column
        }
        data.update(self.additional_data())
        return self.api_client.delete(self.endpoint, data)
