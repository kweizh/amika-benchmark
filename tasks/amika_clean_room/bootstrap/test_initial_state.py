import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/repo"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_git_repo_initialized():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Git repository not initialized in {PROJECT_DIR}."

def test_benchmark_branch_exists():
    result = subprocess.run(["git", "branch", "--list", "benchmark-branch"], cwd=PROJECT_DIR, capture_output=True, text=True)
    assert "benchmark-branch" in result.stdout, "Branch 'benchmark-branch' does not exist in the repository."
