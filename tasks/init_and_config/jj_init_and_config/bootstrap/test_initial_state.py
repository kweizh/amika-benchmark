import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_jj_binary_available():
    assert shutil.which("jj") is not None, "jj binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_jj_repo_not_initialized():
    assert not os.path.exists(os.path.join(PROJECT_DIR, ".jj")), ".jj directory should not exist initially."
    assert not os.path.exists(os.path.join(PROJECT_DIR, ".git")), ".git directory should not exist initially."
