import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_jj_dir_exists():
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".jj")), ".jj directory not found in project directory."

def test_git_dir_exists():
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".git")), ".git directory not found in project directory."

def test_jj_config_user_name():
    result = subprocess.run(
        ["jj", "config", "get", "user.name"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'jj config get user.name' failed: {result.stderr}"
    assert "Alice" in result.stdout, f"Expected user.name to be 'Alice', got: {result.stdout}"

def test_jj_config_user_email():
    result = subprocess.run(
        ["jj", "config", "get", "user.email"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'jj config get user.email' failed: {result.stderr}"
    assert "alice@example.com" in result.stdout, f"Expected user.email to be 'alice@example.com', got: {result.stdout}"

def test_hello_txt_exists_and_content():
    file_path = os.path.join(PROJECT_DIR, "hello.txt")
    assert os.path.isfile(file_path), "hello.txt not found."
    with open(file_path, "r") as f:
        content = f.read()
    assert "Hello, jj!" in content, f"Expected 'Hello, jj!' in hello.txt, got: {content}"
