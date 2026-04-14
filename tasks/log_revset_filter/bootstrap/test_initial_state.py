import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/repo"

def test_jj_binary_available():
    assert shutil.which("jj") is not None, "jj binary not found in PATH."

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_jj_repository_initialized():
    jj_dir = os.path.join(PROJECT_DIR, ".jj")
    assert os.path.isdir(jj_dir), f"Jujutsu repository not initialized at {jj_dir}."

def test_commits_exist():
    # Verify that commits by Bob exist
    result = subprocess.run(
        ["jj", "log", "-r", "author(\"Bob\")", "-T", "change_id"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "Failed to run jj log to check for Bob's commits."
    assert len(result.stdout.strip()) > 0, "No commits by 'Bob' found in the repository."

def test_main_bookmark_exists():
    # Verify that the main bookmark exists
    result = subprocess.run(
        ["jj", "log", "-r", "main", "-T", "change_id"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "Failed to run jj log to check for 'main' bookmark. Does it exist?"
