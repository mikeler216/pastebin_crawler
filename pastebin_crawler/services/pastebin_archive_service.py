"""

"""
from typing import Generator, Iterator, List

from bs4 import BeautifulSoup

from pastebin_crawler.helpers.logger import info_logging
from pastebin_crawler.services import BaseCrawlerService


class PasteBinArchiveService(BaseCrawlerService):
    """"""

    def __init__(self):
        super(PasteBinArchiveService, self).__init__(
            base_url="https://pastebin.com", resource_url="archive"
        )

    @info_logging
    def get_latest_posts_urls(self) -> List[str]:
        """

        :return:
        """
        _urls = []
        _archive_content: bytes = self._get_url_content()
        html_parser = BeautifulSoup(_archive_content, features="html.parser")
        for i in html_parser.find("div", {"class", "archive-table"}).find_all(
            "a"
        ):
            try:
                _url = i.attrs["href"]
                if "archive" in _url:
                    continue
                _urls.append(_url)
            except (AttributeError, KeyError) as e:
                self._logger.error(exception=e, func="get_latest_posts_urls")
                continue
        return _urls
