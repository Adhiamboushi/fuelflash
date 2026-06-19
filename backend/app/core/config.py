from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # App
    APP_NAME: str = "FuelFlash"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Africa's Talking
    AT_USERNAME: str
    AT_API_KEY: str
    AT_SENDER_ID: str = "FuelFlash"

    class Config:
        env_file = ".env"

settings = Settings()