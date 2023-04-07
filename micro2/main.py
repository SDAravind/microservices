from fastapi import FastAPI
from config.settings import MS2_APPSERVER
app = FastAPI()


@app.get("/microservice1")
def index():
    return {"message": "Hello, from Microservice 1"}


if __name__ == "__main__":
    import uvicorn

    kwargs = {
        "host": MS2_APPSERVER.HOST,
        "port": MS2_APPSERVER.PORT,
        "reload": MS2_APPSERVER.RELOAD,
        "workers": None if MS2_APPSERVER.RELOAD else 2
    }

    uvicorn.run("main:app", **kwargs)
