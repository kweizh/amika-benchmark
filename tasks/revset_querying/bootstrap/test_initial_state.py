import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_jj_binary_available():
    assert shutil.which("jj") is not None, "jj binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), "Project directory not found."

def test_main_bookmark_exists():
    result = subprocess.run(["jj", "bookmark", "list"], capture_output=True, text=True, cwd=PROJECT_DIR)
    assert "main" in result.stdout, "Expected 'main' bookmark in jj bookmark list."
