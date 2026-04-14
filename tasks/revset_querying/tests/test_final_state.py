import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_revset_txt_exists():
    assert os.path.isfile(os.path.join(PROJECT_DIR, "revset.txt")), "revset.txt should exist."

def test_revset_evaluates_correctly():
    with open(os.path.join(PROJECT_DIR, "revset.txt"), "r") as f:
        revset = f.read().strip()
    
    result = subprocess.run(
        ["jj", "log", "-T", "description", "-r", revset],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'jj log' failed with revset '{revset}': {result.stderr}"
    assert "Bob 1" in result.stdout, "Expected 'Bob 1' in revset evaluation."
    assert "Bob 2" in result.stdout, "Expected 'Bob 2' in revset evaluation."
    assert "Alice 1" not in result.stdout, "Expected 'Alice 1' to NOT be in revset evaluation."
    assert "Base commit" not in result.stdout, "Expected 'Base commit' to NOT be in revset evaluation."