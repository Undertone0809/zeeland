import os
import tempfile
from unittest.mock import patch

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


def test_get_default_storage_path_permission_error():
    # Mock os.makedirs to raise PermissionError on first call, then succeed
    with patch("os.makedirs") as mock_makedirs:
        mock_makedirs.side_effect = [PermissionError, None]

        # Get the expected temp directory path
        expected_temp_base = convert_backslashes(
            os.path.join(tempfile.gettempdir(), "zeeland")
        )

        # Test single framework with permission error
        result = get_default_storage_path("test_framework")
        assert result == f"{expected_temp_base}/test_framework"

        # Test framework with module with permission error
        mock_makedirs.side_effect = [PermissionError, None]  # Reset side effect
        result = get_default_storage_path("test_framework", "test_module")
        assert result == f"{expected_temp_base}/test_framework/test_module"
