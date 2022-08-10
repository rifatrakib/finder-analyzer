from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    MONGO_URI: str
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_AUTH: str
    
    class Config:
        env_file = ".env"
