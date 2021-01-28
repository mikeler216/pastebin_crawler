from urllib import parse


class BaseCrawlerService(object):
    def __init__(self, base_url: str, archive_url: str):
        """

        :param archive_url:
        :param base_url:
        """
        self._archive_url: str = archive_url
        self._base_url: str = base_url

    @property
    def archive_url(self) -> str:
        """

        :return:
        """
        return parse.urljoin(base=self._base_url, url=self._archive_url)

    # def get_a
