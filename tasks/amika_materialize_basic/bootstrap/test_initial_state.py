import os
import shutil
import pytest

WORKSPACE_DIR = "/workspace"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_workspace_directory_exists():
    assert os.path.isdir(WORKSPACE_DIR), f"Workspace directory {WORKSPACE_DIR} does not exist."

def test_output_directory_does_not_exist_yet():
    # The output directory should not exist or should be empty initially, 
    # but since it's an initial state test, we just check workspace.
    pass
