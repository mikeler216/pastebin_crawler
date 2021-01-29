from urllib import parse

import requests
from requests import Response

from pastebin_crawler.helpers.exceptions_helper import GateWayError
from pastebin_crawler.helpers.logger import info_logging


class BaseCrawlerService(object):
    def __init__(self, base_url: str, resource_url: str):
        """

        :param resource_url:
        :param base_url:
        """
        self._resource_url: str = resource_url
        self._base_url: str = base_url

    @property
    def base_url(self) -> str:
        """

        :return:
        """
        return self._base_url

    @property
    def resource_url(self) -> str:
        """

        :return:
        """
        return parse.urljoin(base=self._base_url, url=self._resource_url)

    def handle_response(self, response: Response) -> Response:
        """

        :param response:
        :return:
        """
        if _status_code := response.status_code != 200:
            GateWayError(
                status_code=_status_code, message=f"{response.content}"
            )
        return response

    @info_logging
    def _get_url_content(self) -> bytes:
        """

        :return:
        """
        _response = requests.get(f"{self.resource_url}")
        _response = self.handle_response(response=_response)
        return _response.content
