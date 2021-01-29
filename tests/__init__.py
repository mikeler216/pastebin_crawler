import uuid
from datetime import datetime

from faker import Faker

faker = Faker()


class FakePostData(object):
    @property
    def fake_author(self) -> str:
        return faker.name()

    @property
    def fake_post_date(self) -> datetime:
        return faker.date_time()

    @property
    def fake_post_text(self) -> str:
        return "\n".join([faker.tet(max_nb_chars=160) for _ in range(20)])

    @property
    def fake_pastebin_id(self) -> str:
        return uuid.uuid4().hex[:5]
