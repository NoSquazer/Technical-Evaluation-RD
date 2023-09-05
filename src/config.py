# Python
import os

# Pydantic
from pydantic import BaseSettings

env_path = os.path.join(os.getcwd(), ".env")


class Settings(BaseSettings):
    class Config:
        case_sensitive = False
        env_file = env_path
        env_file_encoding = "utf-8"

    DB_URL: str
    PROJECT_NAME: str
    API_V1_STR: str


settings = Settings()
