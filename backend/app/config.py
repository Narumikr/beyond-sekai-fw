from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    app_name: str = "Sekai Backend"
    debug: bool = False
    openapi_enabled: bool = False

    model_config = SettingsConfigDict(
        env_prefix="APP_", env_file=".env", extra="ignore"
    )


class CORSSettings(BaseSettings):
    allow_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(
        env_prefix="CORS_", env_file=".env", extra="ignore"
    )


app_settings = AppSettings()
cors_settings = CORSSettings()
