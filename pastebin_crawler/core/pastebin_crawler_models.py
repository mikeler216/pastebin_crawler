from datetime import datetime

from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from pastebin_crawler.settings.config import Config

config: Config = Config()
engine = create_engine(
    f"{config.ENGINE}://{config.DB_USER_NAME}:"
    f"{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=config.DB_ECHO,
)


Base: DeclarativeMeta = declarative_base()

metadata = Base.metadata

DBSession = sessionmaker(bind=engine, autoflush=False)


class Post(Base):
    __tablename__ = "posts"
    id = Column(INTEGER(), primary_key=True, nullable=True, autoincrement=True)
    pastebin_id = Column(VARCHAR(50), unique=True)
    author = Column(VARCHAR(100), nullable=True)
    post_text = Column(TEXT(), nullable=False)
    post_date = Column(TIMESTAMP())
    title = Column(VARCHAR(250), nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(
        TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )


def create_tables(db_engine) -> None:
    """"""
    Base.metadata.create_all(db_engine)
    return None


def create_tables_for_demo_or_test():
    _is_db_ready = False
    _max_tries = 60
    _tries = 0
    while not _is_db_ready:
        _tries += 1
        try:
            engine.connect()
            create_tables(engine)
        except Exception:
            if _tries == _max_tries:
                raise TimeoutError("error starting DB")
        else:
            _is_db_ready = True
            return
