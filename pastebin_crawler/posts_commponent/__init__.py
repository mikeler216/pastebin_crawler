from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.core.pastebin_crawler_models import DBSession
from pastebin_crawler.repository.posts_repository import PostsRepository


class BaseComponent(object):
    """"""

    def __init__(self, db_session: Optional[Session]):
        self._db_session: Optional[Session] = db_session

        self.posts_repository: PostsRepository = PostsRepository(
            db_session=db_session
        )

    @property
    def db_session(self) -> Session:
        """

        :return:
        """
        if self._db_session is None:
            self._db_session: Session = DBSession()
        return self._db_session
