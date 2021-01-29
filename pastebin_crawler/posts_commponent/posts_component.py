from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.helpers import remove_trailing_slash_by_delimiter
from pastebin_crawler.helpers.exceptions_helper import PostExistsError
from pastebin_crawler.helpers.logger import info_logging
from pastebin_crawler.helpers.schemas import PostSchemaBase
from pastebin_crawler.posts_commponent import BaseComponent


class PostsComponent(BaseComponent):
    def __init__(self, db_session: Optional[Session] = None):
        super(PostsComponent, self).__init__(db_session=db_session)

    @info_logging
    def get_post_by_pastebin_id(self, pastebin_id: str) -> Optional[Post]:
        """

        :param pastebin_id:
        :return:
        """
        return self.posts_repository.get_post_by_pastebin_id(
            pastebin_id=pastebin_id
        )

    @info_logging
    def create_post(
        self,
        pastebin_id: str,
        author: str,
        title: str,
        post_text: str,
        post_date: datetime,
        flush: bool = False,
        commit: bool = False,
        validate_exists: bool = True,
    ) -> Post:
        """

        :param validate_exists:
        :param title:
        :param commit:
        :param flush:
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
            title=title,
        )

        if validate_exists and self.get_post_by_pastebin_id(
            pastebin_id=pastebin_id
        ):
            raise PostExistsError(
                f"Post with pastbin ID: {_post.pastebin_id} exists"
            )

        return self.posts_repository.create_post(
            pastebin_id=_post.pastebin_id,
            title=title,
            author=_post.author,
            post_text=_post.post_text,
            post_date=_post.post_date,
            flush=flush,
            commit=commit,
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
