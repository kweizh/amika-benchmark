import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_sandbox_created():
    result = subprocess.run(
        ["amika", "sandbox", "list"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "dev-sandbox" in result.stdout, f"Expected 'dev-sandbox' in 'amika sandbox list' output, got: {result.stdout}"

def test_output_file_exists_and_content_is_correct():
    output_path = os.path.join(PROJECT_DIR, "output.txt")
    assert os.path.isfile(output_path), f"File {output_path} does not exist on the host. The mount mode may not be 'rw'."
    
    with open(output_path, "r") as f:
        content = f.read().strip()
    
    assert content == "hello from sandbox", f"Expected content 'hello from sandbox', got: '{content}'"
