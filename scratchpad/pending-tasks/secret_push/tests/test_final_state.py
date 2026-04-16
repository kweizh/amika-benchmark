import os
import subprocess
import pytest

def test_secret_stored_via_cli():
    """Priority 1: Use amika CLI to verify the secret is stored."""
    # Try `amika secret list`
    result = subprocess.run(
        ["amika", "secret", "list"],
        capture_output=True, text=True, cwd="/home/user/workspace"
    )
    if result.returncode == 0:
        assert "OPENAI_API_KEY" in result.stdout or "OPENAI_API_KEY" in result.stderr, \
            f"Expected 'OPENAI_API_KEY' in secret list, got: {result.stdout} {result.stderr}"
    else:
        # Fallback to checking ~/.amika
        config_dir = "/root/.amika"
        if os.path.isdir(config_dir):
            found = False
            for root, _, files in os.walk(config_dir):
                for f in files:
                    try:
                        with open(os.path.join(root, f), 'r') as file:
                            content = file.read()
                            if "OPENAI_API_KEY" in content:
                                found = True
                                break
                    except Exception:
                        pass
                if found:
                    break
            assert found, "Secret OPENAI_API_KEY not found in amika state or CLI output."
        else:
            pytest.fail("Could not verify secret: `amika secret list` failed and ~/.amika not found.")