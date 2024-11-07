import os

import pytest

from zeeland import Logger, get_default_storage_path
from zeeland.logger import ExceptionHandler


@pytest.fixture
def logger():
    logger = Logger("test")
    yield logger


def test_logger_creation(logger):
    assert isinstance(logger, Logger)
    assert logger.name == "test"


def test_logger_file_creation(logger):
    log_dir = os.path.join(get_default_storage_path("test"), "logs")
    assert os.path.exists(log_dir)
    log_files = os.listdir(log_dir)
    assert len(log_files) > 0


def test_logger_logging(logger):
    test_message = "Test log message"
    logger.info(test_message)

    log_dir = os.path.join(get_default_storage_path("test"), "logs")
    log_files = os.listdir(log_dir)
    latest_log = max(log_files)

    with open(os.path.join(log_dir, latest_log), "r") as f:
        log_content = f.read()
        assert test_message in log_content


def test_exception_handling(logger):
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        logger.error("Error occurred: %s", str(e))

    log_dir = os.path.join(get_default_storage_path("test"), "logs")
    log_files = os.listdir(log_dir)
    latest_log = max(log_files)

    with open(os.path.join(log_dir, latest_log), "r") as f:
        log_content = f.read()
        assert "Test exception" in log_content


def test_multiple_loggers():
    logger1 = Logger("test1")
    logger2 = Logger("test2")

    test_message1 = "Test message 1"
    test_message2 = "Test message 2"

    logger1.info(test_message1)
    logger2.info(test_message2)

    # Check logger1's log file
    log_dir1 = os.path.join(get_default_storage_path("test1"), "logs")
    log_files1 = os.listdir(log_dir1)
    latest_log1 = max(log_files1)

    with open(os.path.join(log_dir1, latest_log1), "r") as f:
        log_content = f.read()
        assert test_message1 in log_content
        assert test_message2 not in log_content

    # Check logger2's log file
    log_dir2 = os.path.join(get_default_storage_path("test2"), "logs")
    log_files2 = os.listdir(log_dir2)
    latest_log2 = max(log_files2)

    with open(os.path.join(log_dir2, latest_log2), "r") as f:
        log_content = f.read()
        assert test_message2 in log_content
        assert test_message1 not in log_content


def test_exception_handler_registration():
    # Clear existing observers
    ExceptionHandler._observers.clear()

    logger1 = Logger("test1")
    logger2 = Logger("test2")

    assert logger1 in ExceptionHandler._observers
    assert logger2 in ExceptionHandler._observers
    assert len(ExceptionHandler._observers) == 2


def test_multiple_loggers_exception_handling():
    logger1 = Logger("test1")
    logger2 = Logger("test2")

    try:
        raise ValueError("Test multi-logger exception")
    except ValueError:
        ExceptionHandler.handle_exception(
            ValueError, ValueError("Test multi-logger exception"), None
        )

    # Check logger1's log file
    log_dir1 = os.path.join(get_default_storage_path("test1"), "logs")
    log_files1 = os.listdir(log_dir1)
    latest_log1 = max(log_files1)

    with open(os.path.join(log_dir1, latest_log1), "r") as f:
        log_content = f.read()
        assert "Test multi-logger exception" in log_content
        assert "Uncaught exception" in log_content

    # Check logger2's log file
    log_dir2 = os.path.join(get_default_storage_path("test2"), "logs")
    log_files2 = os.listdir(log_dir2)
    latest_log2 = max(log_files2)

    with open(os.path.join(log_dir2, latest_log2), "r") as f:
        log_content = f.read()
        assert "Test multi-logger exception" in log_content
        assert "Uncaught exception" in log_content


def test_keyboard_interrupt_handling():
    logger1 = Logger("test1")
    logger2 = Logger("test2")

    # Test KeyboardInterrupt handling
    ExceptionHandler.handle_exception(KeyboardInterrupt, KeyboardInterrupt(), None)

    # Check that KeyboardInterrupt was not logged
    log_dir1 = os.path.join(get_default_storage_path("test1"), "logs")
    log_files1 = os.listdir(log_dir1)
    latest_log1 = max(log_files1)

    with open(os.path.join(log_dir1, latest_log1), "r") as f:
        log_content = f.read()
        assert "KeyboardInterrupt" not in log_content

    log_dir2 = os.path.join(get_default_storage_path("test2"), "logs")
    log_files2 = os.listdir(log_dir2)
    latest_log2 = max(log_files2)

    with open(os.path.join(log_dir2, latest_log2), "r") as f:
        log_content = f.read()
        assert "KeyboardInterrupt" not in log_content
