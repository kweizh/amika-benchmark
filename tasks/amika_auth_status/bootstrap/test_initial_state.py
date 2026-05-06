import os
import shutil
import pytest

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_amika_api_key_configured():
    assert "AMIKA_API_KEY" in os.environ, "AMIKA_API_KEY environment variable is not set."

def test_project_dir_exists():
    assert os.path.isdir("/home/user"), "/home/user directory does not exist."
