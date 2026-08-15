from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    postgres_host: str = "postgres"
    postgres_port: int = 5432
    postgres_user: str
    postgres_password: str
    postgres_db: str

    fetch_interval_minutes: int = 10 # might change to day later ?


settings = Settings()
