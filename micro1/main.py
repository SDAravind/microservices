from fastapi import FastAPI
from config.settings import MS1_APPSERVER

app = FastAPI()


@app.get("/microservice1")
def index():
    return {"message": "Hello, from Microservice 1"}


if __name__ == "__main__":
    import uvicorn

    kwargs = {
        "host": MS1_APPSERVER.HOST,
        "port": MS1_APPSERVER.PORT,
        "reload": MS1_APPSERVER.RELOAD,
        "workers": None if MS1_APPSERVER.RELOAD else 2
    }

    uvicorn.run("main:app", **kwargs)
