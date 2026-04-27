import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_is_git_repository():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Git repository not found at {git_dir}."

def test_package_json_exists():
    pkg_json = os.path.join(PROJECT_DIR, "package.json")
    assert os.path.isfile(pkg_json), f"package.json not found at {pkg_json}."
