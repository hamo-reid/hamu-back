from fastapi import FastAPI
from settings import APPSettings

app_settings = APPSettings()


app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=app_settings.is_reload,
    )
