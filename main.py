import logging

from config import Config
from api_client import APIClient
from megaverse_map import MegaverseMap

def main():
    config = Config()
    api_client = APIClient(config)

    megaverse_map = MegaverseMap(api_client)
    megaverse_map.create_map()

if __name__ == "__main__":
    main()
