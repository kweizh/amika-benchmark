import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/frontend-app"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_git_repo_initialized():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Git repository not initialized in {PROJECT_DIR}."

def test_index_html_exists():
    index_path = os.path.join(PROJECT_DIR, "index.html")
    assert os.path.isfile(index_path), f"index.html not found at {index_path}."
    with open(index_path, "r") as f:
        content = f.read()
    assert "Hello from frontend" in content, "index.html does not contain 'Hello from frontend'."
