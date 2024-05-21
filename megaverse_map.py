from logging_config import logger 
from objects.astral_object_factory import AstralObjectFactory

class MegaverseMap:
    def __init__(self, api_client):
        self.api_client = api_client
        self.grid = None

    def fetch_map_goal(self):
        logger.info("Fetching map goal...")
        self.grid = self.api_client.get_map_goal()
        logger.info("Map goal fetched successfully.")

    def create_map(self):
        if self.grid is None:
            self.fetch_map_goal()
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell == "SPACE":
                    continue  # Skip space cells
                try:
                    obj = AstralObjectFactory.create_astral_object(cell, row_idx, col_idx, self.api_client)
                    obj.create()
                    logger.info(f"{obj.__class__.__name__} created at ({row_idx}, {col_idx}).")
                except Exception as e:
                    logger.error(f"Failed to create {obj.__class__.__name__} at ({row_idx}, {col_idx}): {e}")

    def delete_map(self):
        if self.grid is None:
            self.fetch_map_goal()
        
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell == "SPACE":
                    continue  # Skip space cells
                try:
                    obj = AstralObjectFactory.create_astral_object(cell, row_idx, col_idx, self.api_client)
                    print(obj)
                    obj.delete()
                    logger.info(f"{obj.__class__.__name__} deleted at ({row_idx}, {col_idx}).")
                except Exception as e:
                    logger.error(f"Failed to delete {obj.__class__.__name__} at ({row_idx}, {col_idx}): {e}")

