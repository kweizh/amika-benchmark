import subprocess
import json
import pytest

def test_sandbox_created_via_cli():
    """Priority 1: Use Amika CLI to verify the sandbox is created."""
    result = subprocess.run(
        ["amika", "sandbox", "list", "--json"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"'amika sandbox list --json' failed: {result.stderr}"
    
    try:
        sandboxes = json.loads(result.stdout)
    except json.JSONDecodeError:
        # If --json is not supported or returns non-JSON, fallback to text check
        assert "harbor-sandbox-test" in result.stdout, \
            f"Expected 'harbor-sandbox-test' in output, got: {result.stdout}"
        return

    # Check if the sandbox is in the JSON list
    # Assuming list returns array of objects with a 'name' field
    app_names = [s.get("name") for s in sandboxes if "name" in s]
    
    # If the JSON structure is different, fallback to string check
    if not app_names and sandboxes:
        assert "harbor-sandbox-test" in result.stdout, \
            f"Expected 'harbor-sandbox-test' in output, got: {result.stdout}"
    else:
        assert "harbor-sandbox-test" in app_names, \
            f"Expected 'harbor-sandbox-test' in deployed sandboxes, got: {app_names}"
