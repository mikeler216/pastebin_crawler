from typing import Set


class Urls:
    paste_bin: str = "https://pastebin.com"


class PostDivName:
    username: str = "username"
    title: str = "info-top"
    post_text: str = "textarea"
    post_date: str = "date"


class ValuesToNormalize:
    untitled = "Untitled"
    guest: str = "Guest"
    anonymous: str = "Anonymous"
    ALL_VALUES: Set[str] = {untitled, anonymous, guest}
