"""

"""

import pytest
from pydantic import ValidationError
from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.helpers.exceptions_helper import PostExistsError
from pastebin_crawler.helpers.typings_helper import FakePostData
from pastebin_crawler.posts_commponent.posts_component import PostsComponent


def test_create_user_failed(
    random_post: Post, db_session: Session, fake_post_data: FakePostData
):
    """

    :param random_post:
    :param db_session:
    :param fake_post_data:
    :return:
    """
    posts_component: PostsComponent = PostsComponent(db_session=db_session)

    _author = fake_post_data.fake_author
    _post_text = fake_post_data.fake_post_text
    _pastebin_id = fake_post_data.fake_pastebin_id
    _title = fake_post_data.fake_title

    # test wrong schema
    with pytest.raises(ValidationError):
        posts_component.create_post(
            pastebin_id=_pastebin_id,
            author=_author,
            title=_title,
            post_text=_post_text,
            post_date=["", "sadasasd", "sadsadas"],
        )  # noqa

    # test duplicate post
    with pytest.raises(PostExistsError):
        posts_component.create_post(
            pastebin_id=random_post.pastebin_id,
            author=random_post.author,
            title=_title,
            post_text=random_post.post_text,
            post_date=random_post.post_date,
        )


def test_create_user(db_session: Session, fake_post_data: FakePostData):
    _author = fake_post_data.fake_author
    _post_date = fake_post_data.fake_post_date
    _post_text = fake_post_data.fake_post_text
    _pastebin_id = fake_post_data.fake_pastebin_id
    _title = fake_post_data.fake_title

    posts_component: PostsComponent = PostsComponent(db_session=db_session)

    _new_post = posts_component.create_post(
        pastebin_id=_pastebin_id,
        author=_author,
        title=_title,
        post_text=_post_text,
        post_date=_post_date,
        commit=True,
    )

    _new_post_from_db = posts_component.get_post_by_pastebin_id(
        pastebin_id=_new_post.pastebin_id
    )

    assert _author == _new_post_from_db.author
    assert _post_date == _new_post_from_db.post_date
    assert _post_text == _new_post_from_db.post_text
    assert _pastebin_id == _new_post_from_db.pastebin_id
    assert _title == _new_post_from_db.title
