from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_CONNECTION: str
    SECRET_KEY: str
    EXP_TIME: int
    ALGORITHM: str


settings = Settings()
