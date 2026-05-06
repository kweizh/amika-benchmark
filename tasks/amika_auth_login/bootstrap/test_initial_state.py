import os
import shutil
import pytest

PROJECT_DIR = "/home/user"
KEY_FILE = os.path.join(PROJECT_DIR, "amika_key.txt")

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_key_file_exists():
    assert os.path.isfile(KEY_FILE), f"API key file {KEY_FILE} does not exist."

def test_key_file_not_empty():
    with open(KEY_FILE, "r") as f:
        content = f.read().strip()
    assert len(content) > 0, f"API key file {KEY_FILE} is empty."
