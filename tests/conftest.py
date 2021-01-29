import uuid

import pytest
from faker import Faker
from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import (
    create_deals_table,
    engine,
    DBSession,
    Post,
)
from pastebin_crawler.helpers.typings_helper import FakePostData
from pastebin_crawler.repository.posts_repository import PostsRepository


@pytest.fixture(scope="module")
def db_session() -> Session:
    """
    Create tables and remove them at end of test
    THIS SHOULD NOT BE RUN ON REAL DB EVER only through a reusable compose test!!!
    :return: db session object
    """
    create_deals_table(engine)
    session = DBSession()
    try:
        yield session
    finally:
        session.query(Post).delete()
        session.commit()


@pytest.fixture(
    scope="function",
)
def fake_post_data() -> FakePostData:
    faker = Faker()
    return FakePostData(
        fake_author=faker.name(),
        fake_post_date=faker.date_time(),
        fake_post_text="\n".join(
            [faker.text(max_nb_chars=160) for _ in range(20)]
        ),
        fake_pastebin_id=uuid.uuid4().hex[:5],
    )


@pytest.fixture(scope="function")
def random_post(fake_post_data, db_session) -> Post:

    posts_repository = PostsRepository(db_session=db_session)

    _post: Post = posts_repository.create_post(
        pastebin_id=fake_post_data.fake_pastebin_id,
        post_text=fake_post_data.fake_post_text,
        post_date=fake_post_data.fake_post_date,
        author=fake_post_data.fake_author,
        commit=True,
    )

    yield _post

    db_session.query(Post).delete()
