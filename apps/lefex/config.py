from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG : bool = False
    DATABASE_URL : str = ""

    class Config:
        env_file = './.env'


