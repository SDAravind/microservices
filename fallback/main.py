from fastapi import FastAPI

from config.settings import FB_APPSERVER

app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    kwargs = {
        "host": FB_APPSERVER.HOST,
        "port": FB_APPSERVER.PORT,
        "reload": FB_APPSERVER.RELOAD,
        "workers": None if FB_APPSERVER.RELOAD else 2,
    }

    uvicorn.run("main:app", **kwargs)
