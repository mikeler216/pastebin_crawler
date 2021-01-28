def remove_trailing_slash_by_delimiter(text: str, delimiter: str) -> str:
    """

    :param text:
    :param delimiter:
    :return:
    """
    return "\n".join([_text.strip() for _text in text.split(delimiter)])
