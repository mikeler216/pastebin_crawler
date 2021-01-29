from urllib import parse

import requests

from pastebin_crawler.services.pastebin_archive_service import (
    PasteBinArchiveService,
)


def test_service_archive():
    """

    :return:
    """
    pastebin_archive_service: PasteBinArchiveService = PasteBinArchiveService()

    _latest_posts_href = pastebin_archive_service.get_latest_posts_urls()

    # test if the href links are real links
    for _post_href in _latest_posts_href:
        assert (
            requests.get(
                url=parse.urljoin(
                    pastebin_archive_service.base_url, _post_href
                )
            ).status_code
            == 200
        )
        break
