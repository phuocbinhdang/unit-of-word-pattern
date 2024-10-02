import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseConfiguration:
    DATABASE_URL = os.getenv("DATABASE_URL", "")
