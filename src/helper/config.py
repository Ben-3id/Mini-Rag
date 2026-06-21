from pydantic_settings import BaseSettings ,SettingsConfigDict


class settings(BaseSettings):
    PROJECT_NAME:str 
    PROJECT_VERSION:str

    FILE_ALLOWED_EXTENTIONS :list
    FILE_MAX_SIZE : int

    class config:
        file = ".env"

def get_settings():
    return settings()

