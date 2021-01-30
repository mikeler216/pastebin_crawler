from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import Session, Query, load_only

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

    def get_post_by_pastebin_id(
        self, pastebin_id: str, posts_only: List[str] = None
    ) -> Optional[Post]:
        """

        :param posts_only:
        :param pastebin_id:
        :return:
        """
        _query: Query = self.db_session.query(Post).filter(
            Post.pastebin_id == pastebin_id
        )

        if posts_only:
            _query = _query.options(load_only(*posts_only))

        return _query.one_or_none()
