"""

"""
from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup
import dateutil.parser

from pastebin_crawler.helpers import remove_beginning_slash_from_str
from pastebin_crawler.helpers.constants import Urls, PostDivName
from pastebin_crawler.services import BaseCrawlerService


class PasteBinPostService(BaseCrawlerService):
    def __init__(self, resource_url: str):
        super(PasteBinPostService, self).__init__(
            base_url=Urls.paste_bin, resource_url=resource_url
        )

        self._post_date: Optional[datetime] = None
        self._title: Optional[str] = None
        self._author: Optional[str] = None
        self._post_text: Optional[str] = None
        self._content: bytes = self._get_url_content()
        self._html_parser: Optional[BeautifulSoup] = None

    @property
    def html_parser(self) -> BeautifulSoup:
        if self._html_parser is None:
            self._html_parser = BeautifulSoup(
                self._content, features="html.parser"
            )
        return self._html_parser

    @property
    def pastebin_id(self) -> str:
        """

        :return:
        """
        return remove_beginning_slash_from_str(self._resource_url)

    @property
    def author(self) -> str:
        if self._author is None:
            self._author = (
                self.html_parser.body.find(
                    "div", {"class": {PostDivName.username}}
                )
                .find("a")
                .attrs["href"]
            )
        return str(self._author)

    @property
    def title(self) -> str:
        if self._title is None:
            self._title = self.html_parser.body.find(
                "div", {"class": PostDivName.title}
            ).text
        return str(self._title)

    @property
    def post_text(self) -> str:
        if self._post_text is None:
            self._post_text = self.html_parser.body.find(
                "textarea", {"class": PostDivName.post_text}
            ).text
        return str(self._post_text)

    @property
    def post_date(self) -> datetime:
        if self._post_date is None:
            __post_date: str = (
                self.html_parser.body.find(
                    "div", {"class": PostDivName.post_date}
                )
                .find("span")
                .attrs["title"]
            )
            self._post_date = dateutil.parser.parse(
                __post_date, tzinfos={"CDT": -5 * 3600}
            )
        return self._post_date
