from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from core.settings import settings



class DatabaseConnection():
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False
        )

    async def session_creation(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

db_conn = DatabaseConnection(url=settings.db.url, echo=settings.db.echo)