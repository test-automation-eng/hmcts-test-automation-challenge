import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

LOCKED_USERNAME = os.getenv("LOCKED_USERNAME")
LOCKED_PASSWORD = os.getenv("LOCKED_PASSWORD")
