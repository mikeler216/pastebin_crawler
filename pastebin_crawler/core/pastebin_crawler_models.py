from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, TEXT, TIMESTAMP
from sqlalchemy.orm import sessionmaker

from pastebin_crawler.settings.config import Config
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy_utils import database_exists, create_database

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


def create_deals_table(engine) -> None:
    """"""
    Base.metadata.create_all(engine)
    return None
