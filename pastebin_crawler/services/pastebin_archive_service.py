"""

"""
from typing import Generator, Iterator, List

from bs4 import BeautifulSoup

from pastebin_crawler.services import BaseCrawlerService


class PasteBinArchiveService(BaseCrawlerService):
    """"""

    def __init__(self):
        super(PasteBinArchiveService, self).__init__(
            base_url="https://pastebin.com", resource_url="archive"
        )

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
            _url = i.attrs["href"]
            if "archive" in _url:
                continue
            try:
                _urls.append(_url)
            except (AttributeError, KeyError):
                # todo log
                continue
        return _urls
