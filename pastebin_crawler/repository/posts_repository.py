from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import Post
from pastebin_crawler.repository import RepositoryBase


class PostsRepository(RepositoryBase):
    """"""

    def __init__(self, db_session: Optional[Session] = None):
        super(PostsRepository, self).__init__(db_session=db_session)

    def create_post(
        self,
        pastebin_id: str,
        title: str,
        author: str,
        post_text: str,
        post_date: datetime,
        flush: bool = False,
        commit: bool = False,
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
        _post: Post = Post(
            pastebin_id=pastebin_id,
            author=author,
            post_text=post_text,
            post_date=post_date,
            title=title,
        )
        return self._add_commit_or_flush_model(
            model=_post, commit=commit, flush=flush
        )

    def get_post_by_pastebin_id(self, pastebin_id: str) -> Optional[Post]:
        """

        :param pastebin_id:
        :return:
        """
        return (
            self.db_session.query(Post)
            .filter(Post.pastebin_id == pastebin_id)
            .one_or_none()
        )
