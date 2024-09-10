from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os 

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
SECRET: str = os.environ.get("SECRET")

class DBConfig(BaseModel):
    url: str = DB_URL
    echo: bool = True

class JWTConfig(BaseModel):
    secret: str = SECRET

class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    token: JWTConfig = JWTConfig()


settings = Settings()