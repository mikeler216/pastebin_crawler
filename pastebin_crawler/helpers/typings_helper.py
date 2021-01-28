from dataclasses import dataclass
from datetime import datetime


@dataclass
class FakePostData:
    fake_pastebin_id: str
    fake_author: str
    fake_post_text: str
    fake_post_date: datetime
