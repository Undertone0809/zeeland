import datetime
import logging
import sys
import traceback
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from zeeland import get_default_storage_path


class ExceptionHandler:
    _observers = []

    @classmethod
    def register(cls, logger):
        cls._observers.append(logger)

        # register it when the first time
        if len(cls._observers) == 1:
            sys.excepthook = cls.handle_exception

    @classmethod
    def handle_exception(cls, exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return

        for logger in cls._observers:
            logger.error(
                "Uncaught exception:\n%s",
                "".join(traceback.format_exception(exc_type, exc_value, exc_tb)),
            )

        sys.__excepthook__(exc_type, exc_value, exc_tb)


class Logger(logging.Logger):
    def __init__(self, framework: str):
        super().__init__(framework, logging.DEBUG)
        log_dir = Path(get_default_storage_path(framework, "logs"))
        log_file = log_dir / f"{datetime.datetime.now().strftime('%Y%m%d')}.log"

        handler = TimedRotatingFileHandler(
            filename=log_file, when="midnight", interval=1, encoding="utf-8"
        )
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",  # noqa
            "%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        self.addHandler(handler)

        ExceptionHandler.register(self)
