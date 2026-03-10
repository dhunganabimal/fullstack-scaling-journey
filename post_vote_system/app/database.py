from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Database Config
class Settings(BaseSettings):
    DB_HOSTNAME:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_USERNAME:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE:int

    model_config = {
        "env_file": ".env",
    }
settings=Settings()

#Database Connection
SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}/{settings.DB_NAME}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine )
Base=declarative_base()


def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()