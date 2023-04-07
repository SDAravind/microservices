from pydantic import BaseSettings


class AppServer(BaseSettings):
    HOST: str
    PORT: int
    RELOAD: bool
    WORKERS: int


MS2_APPSERVER = AppServer()
