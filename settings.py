from pydantic import BaseSettings

class APPSettings(BaseSettings):
    host: str = "127.0.0.1"   # sevrer host
    port: int = 8080          # server post 
    is_reload: bool = False   # server reload

    class config:
        env_file = ".env"
        env_file_encoding = 'utf-8'