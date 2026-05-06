import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/test-repo"

def test_restored_sandbox_accessible():
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "git-sandbox-restore", "--", "echo", "alive"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh' failed to connect: {result.stderr}"
    assert "alive" in result.stdout, f"Expected 'alive' from sandbox, got: {result.stdout}"

def test_commit_persists():
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "git-sandbox-restore", "--", "git", "log", "-1", "--oneline"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh' for git log failed: {result.stderr}"
    assert "Add hello.txt" in result.stdout, f"Expected commit message 'Add hello.txt', got: {result.stdout}"

def test_file_exists_in_sandbox():
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "git-sandbox-restore", "--", "cat", "hello.txt"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh cat' failed: {result.stderr}"
    assert "Hello Amika" in result.stdout, f"Expected 'Hello Amika' in hello.txt, got: {result.stdout}"