import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_git_colocated_initialized():
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".jj")), ".jj directory not found. Did you run `jj git init --colocate`?"
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".git")), ".git directory not found. Did you run `jj git init --colocate`?"

def test_user_name_configured():
    result = subprocess.run(["jj", "config", "list", "user.name"], cwd=PROJECT_DIR, capture_output=True, text=True)
    assert "Alice Developer" in result.stdout, f"Expected user.name to be 'Alice Developer', got: {result.stdout}"

def test_user_email_configured():
    result = subprocess.run(["jj", "config", "list", "user.email"], cwd=PROJECT_DIR, capture_output=True, text=True)
    assert "alice@example.com" in result.stdout, f"Expected user.email to be 'alice@example.com', got: {result.stdout}"
