from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "project_01"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list = [
        "http://localhost:5173", # Для Frontend
        "http://localhost:3000", # Для Backend
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()
