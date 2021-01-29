def remove_trailing_slash_by_delimiter(text: str, delimiter: str) -> str:
    """

    :param text:
    :param delimiter:
    :return:
    """
    return "\n".join([_text.strip() for _text in text.split(delimiter)])


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]
