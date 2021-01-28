from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.helpers import remove_trailing_slash_by_delimiter
from pastebin_crawler.helpers.exceptions_helper import PostExistsError
from pastebin_crawler.helpers.schems import PostSchemaBase
from pastebin_crawler.posts_commponent import BaseComponent


class PostsComponent(BaseComponent):
    def __init__(self, db_session: Optional[Session] = None):
        super(PostsComponent, self).__init__(db_session=db_session)

    def get_post_by_pastebin_id(self, pastebin_id: str) -> Optional[Post]:
        """

        :param pastebin_id:
        :return:
        """
        return self.posts_repository.get_post_by_pastebin_id(
            pastebin_id=pastebin_id
        )

    def create_post(
        self,
        pastebin_id: str,
        author: str,
        post_text: str,
        post_date: datetime,
    ) -> Post:
        """

        :param pastebin_id:
        :param author:
        :param post_text:
        :param post_date:
        :return:
        """
        _post: PostSchemaBase = PostSchemaBase(
            pastebin_id=pastebin_id,
            author=author,
            post_text=post_text,
            post_date=post_date,
        )

        if self.get_post_by_pastebin_id(pastebin_id=pastebin_id):
            raise PostExistsError(
                f"Post with pastbin ID: {_post.pastebin_id} exists"
            )

        return self.posts_repository.create_post(
            pastebin_id=_post.pastebin_id,
            author=_post.author,
            post_text=_post.post_text,
            post_date=_post.post_date,
        )

    @staticmethod
    def remove_trailing_spaces_from_post(post_text: str) -> str:
        """

        :param post_text:
        :return:
        """
        return remove_trailing_slash_by_delimiter(
            text=post_text, delimiter="\r\n"
        )
