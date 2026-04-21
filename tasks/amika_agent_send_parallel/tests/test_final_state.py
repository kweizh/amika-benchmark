import subprocess
import pytest

def test_sandboxes_created():
    """Priority 1: Use Amika CLI to verify the sandboxes were created locally."""
    result = subprocess.run(
        ["amika", "sandbox", "list", "--local"],
        capture_output=True, text=True, cwd="/home/user/myproject"
    )
    assert result.returncode == 0, \
        f"'amika sandbox list --local' failed: {result.stderr}"
    
    assert "task-1" in result.stdout, \
        f"Expected 'task-1' in local sandboxes list, got: {result.stdout}"
    
    assert "task-2" in result.stdout, \
        f"Expected 'task-2' in local sandboxes list, got: {result.stdout}"
