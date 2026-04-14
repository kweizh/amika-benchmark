import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_jj_initialized():
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".jj")), "jj repository was not initialized."

def test_alias_configured():
    result = subprocess.run(
        ["jj", "config", "list", "aliases.mylog"],
        capture_output=True,
        text=True,
        env={**os.environ, "HOME": "/home/user"}
    )
    assert result.returncode == 0, "Failed to list jj config for aliases.mylog."
    assert '"log"' in result.stdout and '"-r"' in result.stdout and '"@-"' in result.stdout, \
        f"Alias mylog not configured correctly. Output: {result.stdout}"

def test_run_alias():
    result = subprocess.run(
        ["jj", "mylog"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        env={**os.environ, "HOME": "/home/user"}
    )
    assert result.returncode == 0, f"Running 'jj mylog' failed. Error: {result.stderr}"

def test_file_created_and_committed():
    file_path = os.path.join(PROJECT_DIR, "hello.txt")
    assert os.path.isfile(file_path), "hello.txt was not created."
    with open(file_path, "r") as f:
        assert "Hello jj" in f.read(), "hello.txt does not contain 'Hello jj'."
    
    # Verify it was committed (or is in the working copy commit)
    result = subprocess.run(
        ["jj", "log", "-T", "description"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        env={**os.environ, "HOME": "/home/user"}
    )
    assert "Add hello.txt" in result.stdout, "Commit message 'Add hello.txt' not found in log."
