"""

"""
from typing import Optional, Type

from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

from pastebin_crawler.core.pastebin_crawler_models import DBSession, Base


class RepositoryBase(object):
    """"""

    def __init__(self, db_session: Optional[Session]):
        self._db_session: Optional[Session] = db_session

    @property
    def db_session(self) -> Session:
        """

        :return:
        """
        if self._db_session is None:
            self._db_session: Session = DBSession()
        return self._db_session

    def _add_commit_or_flush_model(
        self, model: Type[Base], flush: bool, commit: bool
    ) -> Type[Base]:
        """

        :param model:
        :param flush:
        :param commit:
        :return:
        """
        self._validate_not_flush_and_commit(flush=flush, commit=commit)

        self.db_session.add(model)

        if commit:
            self.db_session.commit()
        else:
            self.db_session.flush()

        return model

    @staticmethod
    def _validate_not_flush_and_commit(commit: bool, flush: bool) -> None:
        """

        :return:
        """
        if _sum := sum([commit, flush]) != 1:
            raise ValueError(
                f"Either flush or commit must be selected"
                f"You chose {'Both' if _sum == 2 else 'Neither'} "
            )

        return None
