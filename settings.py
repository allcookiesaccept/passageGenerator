import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import logging

log_filename = "application.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
    handlers=[logging.FileHandler(log_filename), logging.StreamHandler()],
)
logger = logging.getLogger("OpenAI Logger")

from dotenv import load_dotenv
from models import GPT

class DataManager:
    __instance = None

    @staticmethod
    def get_instance():
        if DataManager.__instance is None:
            DataManager()
        return DataManager.__instance

    def __init__(self):
        if DataManager.__instance is not None:
            raise Exception("DataManger is a singleton class")
        else:
            load_dotenv()
            self.GPT = self.get_token()
            DataManager.__instance = self

    def get_token(self) -> GPT:
        token = os.getenv("TOKEN")
        organization = os.getenv("ORGANIZATION")
        return GPT(token=token, organization=organization)
