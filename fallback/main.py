from fastapi import FastAPI

from .fallback import appserver

app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    kwargs = {
        "host": appserver.HOST,
        "port": appserver.PORT,
        "reload": appserver.RELOAD,
        "workers": None if appserver.RELOAD else 2,
    }

    uvicorn.run("main:app", **kwargs)
