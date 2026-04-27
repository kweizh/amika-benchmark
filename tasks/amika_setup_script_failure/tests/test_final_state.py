import subprocess
import pytest

def test_sandbox_created_and_running():
    result = subprocess.run(["amika", "sandbox", "list", "--local"], capture_output=True, text=True)
    assert result.returncode == 0, f"amika sandbox list failed: {result.stderr}"
    
    found = False
    is_running = False
    
    for line in result.stdout.splitlines():
        if "test-sandbox" in line:
            found = True
            if "running" in line:
                is_running = True
            break
            
    assert found, "Sandbox 'test-sandbox' was not found in the local sandbox list."
    assert is_running, "Sandbox 'test-sandbox' is found but not in 'running' state."
