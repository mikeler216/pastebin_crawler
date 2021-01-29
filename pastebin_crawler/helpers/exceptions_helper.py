class BasePastbinCrawlerError(Exception):
    pass


class PostExistsError(BasePastbinCrawlerError):
    pass


class GateWayError(BasePastbinCrawlerError):
    def __init__(self, status_code: int, message: str):
        self.message = f"status code: {status_code}, message: {message}"

    def __str__(self):
        return self.message
