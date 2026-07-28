from functools import lru_cache

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..config import get_settings


@lru_cache
def get_engine():
    settings = get_settings()
    return create_async_engine(settings.database_url, echo=False)

@lru_cache
def get_session_maker():
    return async_sessionmaker(get_engine(), expire_on_commit=False)

async def get_db():
    session_maker = get_session_maker()
    async with session_maker() as session:
        yield session
