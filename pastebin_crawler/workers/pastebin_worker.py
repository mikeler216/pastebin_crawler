import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from sqlalchemy.orm import Session

from pastebin_crawler.helpers.logger import info_logging
from pastebin_crawler.posts_commponent.posts_component import PostsComponent
from pastebin_crawler.services.paste_bin_post_service import (
    PasteBinPostService,
)
from pastebin_crawler.services.pastebin_archive_service import (
    PasteBinArchiveService,
)
from pastebin_crawler.workers import PasteBinWorkerBase


class PasteBinWorker(PasteBinWorkerBase):
    def __init__(self, db_session: Optional[Session] = None):
        super(PasteBinWorker, self).__init__(db_session=db_session)
        self.pastebin_archive_service = PasteBinArchiveService()
        self.posts_component = PostsComponent(db_session=db_session)

    @info_logging
    def _handle_post(self, post_url: str) -> None:
        """

        :param post_url:
        :return:
        """

        if not self.posts_component.get_post_by_pastebin_id(
            pastebin_id=post_url[1:]
        ):
            pastebin_post_service = PasteBinPostService(resource_url=post_url)
            self.posts_component.create_post(
                pastebin_id=pastebin_post_service.pastebin_id,
                author=pastebin_post_service.author,
                title=pastebin_post_service.title,
                post_text=pastebin_post_service.post_text,
                post_date=pastebin_post_service.post_date,
                validate_exists=False,
                flush=False,
                commit=True,
            )
        return None

    @info_logging
    def run(self) -> None:
        with self._logger.logger.contextualize(task_id=str(uuid.uuid4())):
            _post_urls = self.pastebin_archive_service.get_latest_posts_urls()
            with ThreadPoolExecutor(max_workers=10) as executor:
                for _post in _post_urls:
                    try:
                        _res = executor.submit(self._handle_post, _post)
                        res = _res.result()
                        self._logger.info(func="run", message=res)

                    except Exception as e:
                        self._logger.error(
                            func=f"{e.__traceback__}", exception=e
                        )
        return None
