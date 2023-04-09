from pydantic import BaseSettings


class AppServer(BaseSettings):
    HOST: str
    PORT: int
    RELOAD: bool
    WORKERS: int


FB_APPSERVER = AppServer()
