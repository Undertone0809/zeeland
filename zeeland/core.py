import os
import tempfile
from typing import Optional


def convert_backslashes(path: str):
    """Convert all \\ to / of file path."""
    return path.replace("\\", "/")


def get_default_storage_path(framework: str, module_name: Optional[str] = None) -> str:
    """Determines the default storage path for a given framework and optional module.

    This function attempts to create the storage path in the user's home directory
    under ~/.zeeland/{framework}, falling back to a temporary directory if permission
    is denied.

    Args:
        framework (str): The framework name.
        module_name (Optional[str]): The name of the module, if applicable.

    Returns:
        str: The default storage path for the specified framework and module.
    """
    storage_path = os.path.expanduser(f"~/.zeeland/{framework}")

    if module_name:
        storage_path = os.path.join(storage_path, module_name)

    try:
        os.makedirs(storage_path, exist_ok=True)
    except PermissionError:
        temp_path = os.path.join(tempfile.gettempdir(), "zeeland", framework)
        storage_path = (
            os.path.join(temp_path, module_name) if module_name else temp_path
        )
        os.makedirs(storage_path, exist_ok=True)

    return convert_backslashes(storage_path)
