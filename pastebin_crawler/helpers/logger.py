import sys
from functools import wraps
from typing import Any, Callable, Optional

from loguru import logger

from pastebin_crawler.helpers import Singleton
from pastebin_crawler.settings.config import Config

config: Config = Config()


def _set_logger():
    """

    :return:
    """
    _logger = logger

    _format: str = "{extra[func]} {extra[returns]} {time} {level} {message}"
    # _format: str = "{extra[task_id]} {extra[func]} {extra[returns]} {time} {level} {message}"
    _logger.add(
        sys.stderr,
        format=_format,
        level=f"{config.DEBUG_LEVEL}",
        enqueue=False,
    )

    return _logger


class Logger(object, metaclass=Singleton):
    """
    Logger for App
    """

    def __init__(self):
        self.__logger = None

    @property
    def logger(self) -> logger:
        """

        :return:
        """
        if self.__logger is None:
            self.__logger = _set_logger()
        return self.__logger

    def info(self, func: str, message: str, returns: Optional[str] = None):
        """
        INFO Logging
        :return:
        """
        with self.logger.contextualize(func=func, returns=returns):
            self.logger.info(self._format_log_message(message=message))

    def error(self, exception: Exception, func):
        """

        :param exception:
        :param func:
        :return:
        """

        with self.logger.contextualize(func=func, returns="None"):
            self.logger.error(self._format_log_message(message=str(exception)))

    def debug(self, func: str, message: str, returns=None):
        """
        INFO Logging
        :return:
        """
        with self.logger.contextualize(func=func, returns=returns):
            self.logger.debug(self._format_log_message(message=message))

    @staticmethod
    def _format_log_message(message: str) -> str:
        """

        :param message:
        :return:
        """
        return f"extra_args: {message}"


def debug_logging(func: Callable):
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Func to decorate
        :param args:
        :param kwargs:
        :return:
        """
        _func_name = func.__qualname__

        _func_return_value: Any = func(*args, **kwargs)
        Logger().debug(
            message=f"locals: {kwargs}",
            returns=f"{_func_return_value}",
            func=f"{_func_name}",
        )
        return _func_return_value

    return wrapper


def info_logging(func: Callable):
    """
    Decorator for info logging
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Func to decorate
        :param args:
        :param kwargs:
        :return:
        """
        _func_name = func.__qualname__

        _func_return_value: Any = func(*args, **kwargs)
        Logger().info(
            message=f"locals: {kwargs}",
            returns=f"{_func_return_value}",
            func=f"{_func_name}",
        )
        return _func_return_value

    return wrapper
