from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..config import Settings, get_settings


@lru_cache
def get_engine(settings: Settings = Depends(get_settings)):
    return create_async_engine(settings.database_url, echo=False)

@lru_cache
def get_session_maker(engine = Depends(get_engine)):
    return async_sessionmaker(engine, expire_on_commit=False)

async def get_db(session_maker = Depends(get_session_maker)):
    async with session_maker() as session:
        yield session
