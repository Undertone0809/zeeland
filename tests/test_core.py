import os

from zeeland import convert_backslashes, get_default_storage_path


def test_convert_backslashes():
    assert (
        convert_backslashes("C:\\Users\\User\\Documents") == "C:/Users/User/Documents"
    )
    assert convert_backslashes("C:/Users/User/Documents") == "C:/Users/User/Documents"


def test_get_default_storage_path():
    # Use os.path.expanduser to get the expected expanded path
    expected_base = convert_backslashes(os.path.expanduser("~/.zeeland"))

    # Test single framework
    assert (
        get_default_storage_path("test_framework") == f"{expected_base}/test_framework"
    )

    # Test framework with module
    assert (
        get_default_storage_path("test_framework", "test_module")
        == f"{expected_base}/test_framework/test_module"
    )

    # Test negative case
    assert (
        get_default_storage_path("test_framework", "test_module")
        != f"{expected_base}/Users/User/test_module"
    )
