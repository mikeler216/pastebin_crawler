"""

"""

import pytest
from pydantic import ValidationError
from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.helpers.exceptions_helper import PostExistsError
from pastebin_crawler.helpers.typings_helper import FakePostData
from pastebin_crawler.posts_commponent.posts_component import PostsComponent


def test_create_user(
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
    _post_date = fake_post_data.fake_post_date
    _post_text = fake_post_data.fake_post_text
    _pastebin_id = fake_post_data.fake_pastebin_id

    # test wrong schema
    with pytest.raises(ValidationError):
        posts_component.create_post(
            author=_author,
            post_date=["", "sadasasd", "sadsadas"],
            post_text=_post_text,
            pastebin_id=_pastebin_id,
        )  # noqa

    # test duplicate post
    with pytest.raises(PostExistsError):
        posts_component.create_post(
            author=random_post.author,
            post_date=random_post.post_date,
            post_text=random_post.post_text,
            pastebin_id=random_post.pastebin_id,
        )

    _new_post = posts_component.create_post(
        author=_author,
        post_date=_post_date,
        post_text=_post_text,
        pastebin_id=_pastebin_id,
    )

    _new_post_from_db = posts_component.get_post_by_pastebin_id(
        pastebin_id=_new_post.pastebin_id
    )

    assert _author == _new_post_from_db.author
    assert _post_date == _new_post_from_db.post_date
    assert _post_text == _new_post_from_db.post_text
    assert _pastebin_id == _new_post_from_db.pastebin_id
