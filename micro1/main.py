from fastapi import FastAPI

from .micro1 import appserver

app = FastAPI()


@app.get("/microservice1")
def index():
    return {"message": "Hello, from Microservice 1"}


if __name__ == "__main__":
    import uvicorn

    kwargs = {
        "host": appserver.HOST,
        "port": appserver.PORT,
        "reload": appserver.RELOAD,
        "workers": None if appserver.RELOAD else 2,
    }

    uvicorn.run("main:app", **kwargs)
