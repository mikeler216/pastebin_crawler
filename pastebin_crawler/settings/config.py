from pydantic import BaseSettings


class Config(BaseSettings):
    """"""

    ENGINE: str
    DB_USER_NAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_ECHO: bool
    DEBUG_LEVEL: str

    class Config:
        env_file = ".env"
