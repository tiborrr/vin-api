from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://vpic:vpic_password@127.0.0.1:5433/vpic_db"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

engine = create_async_engine(settings.database_url, echo=False)
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
