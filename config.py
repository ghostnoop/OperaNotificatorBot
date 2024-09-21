from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url:str
    db_name: str
    token: str
    chat_id:str

    class Config:
        env_file = ".env"


config = Config()
