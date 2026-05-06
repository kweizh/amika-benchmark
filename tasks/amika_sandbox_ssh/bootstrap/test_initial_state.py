import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_project_is_git_repo():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Project directory {PROJECT_DIR} is not a git repository."
