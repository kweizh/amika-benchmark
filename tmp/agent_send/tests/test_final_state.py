import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_amika_agent_send_output():
    """Priority 1: Use amika CLI to materialize the file and verify content."""
    # Ensure the output directory exists
    output_dir = os.path.join(PROJECT_DIR, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Materialize the file created by the agent
    result = subprocess.run(
        ["amika", "materialize", "--cmd", "cat hello.txt", "--destdir", output_dir],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika materialize' failed: {result.stderr}"
    
    # Read the materialized file
    hello_file_path = os.path.join(output_dir, "hello.txt")
    assert os.path.isfile(hello_file_path), f"hello.txt was not materialized to {hello_file_path}"
    
    with open(hello_file_path, "r") as f:
        content = f.read().strip()
        
    assert "hello world" in content.lower(), f"Expected 'hello world' in hello.txt, got: {content}"
