"""

"""
from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.helpers.typings_helper import FakePostData
from pastebin_crawler.repository.posts_repository import PostsRepository


def test_create_user(db_session: Session, fake_post_data: FakePostData):
    _author = fake_post_data.fake_author
    _post_date = fake_post_data.fake_post_date
    _post_text = fake_post_data.fake_post_text
    _pastebin_id = fake_post_data.fake_pastebin_id

    posts_repository = PostsRepository(db_session=db_session)

    _post: Post = posts_repository.create_post(
        pastebin_id=_pastebin_id,
        post_text=_post_text,
        post_date=_post_date,
        commit=True,
        author=_author,
    )

    assert _post.author == _author
    assert _post.post_date == _post_date
    assert _post.post_text == _post_text
    assert _post.pastebin_id == _pastebin_id
    assert type(_post.id) is int


def test_get_post_by_pastebin_id(random_post: Post, db_session: Session):
    posts_repository = PostsRepository(db_session=db_session)

    post: Optional[Post] = posts_repository.get_post_by_pastebin_id(
        pastebin_id=random_post.pastebin_id
    )

    assert post is not None

    assert post.id == random_post.id
    assert post.pastebin_id == random_post.pastebin_id
    assert post.author == random_post.author
    assert post.post_text == random_post.post_text
    assert post.post_date == random_post.post_date
