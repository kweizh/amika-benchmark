import os
import subprocess
import json
import shutil
import pytest

PROJECT_DIR = "/home/user/project"
WRAPPER_SCRIPT = os.path.join(PROJECT_DIR, "amika_wrapper.sh")

@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup: ensure clean state
    state_dir = os.environ.get("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
    amika_state_dir = os.path.join(state_dir, "amika")
    session_file = os.path.join(amika_state_dir, "workos-session.json")
    
    if os.path.exists(session_file):
        os.remove(session_file)
        
    yield
    
    # Teardown
    if os.path.exists(session_file):
        os.remove(session_file)

def test_wrapper_prioritizes_session_file():
    """Priority 1: Use the wrapper script to verify it unsets AMIKA_API_KEY when session file exists."""
    state_dir = os.environ.get("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
    amika_state_dir = os.path.join(state_dir, "amika")
    os.makedirs(amika_state_dir, exist_ok=True)
    session_file = os.path.join(amika_state_dir, "workos-session.json")
    
    with open(session_file, "w") as f:
        f.write("{}")
        
    env = os.environ.copy()
    env["AMIKA_API_KEY"] = "dummy_key"
    
    result = subprocess.run(
        [WRAPPER_SCRIPT, "auth", "status"],
        capture_output=True, text=True, cwd=PROJECT_DIR, env=env
    )
    
    # When session file exists, the wrapper should unset AMIKA_API_KEY.
    # So amika auth status should NOT say "Authenticated via AMIKA_API_KEY environment variable"
    assert "Authenticated via AMIKA_API_KEY environment variable" not in result.stdout, \
        f"Wrapper script failed to prioritize session file. Output: {result.stdout}"

def test_wrapper_uses_api_key_when_no_session():
    """Priority 1: Use the wrapper script to verify it uses AMIKA_API_KEY when no session file exists."""
    state_dir = os.environ.get("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
    amika_state_dir = os.path.join(state_dir, "amika")
    session_file = os.path.join(amika_state_dir, "workos-session.json")
    
    if os.path.exists(session_file):
        os.remove(session_file)
        
    env = os.environ.copy()
    env["AMIKA_API_KEY"] = "dummy_key"
    
    result = subprocess.run(
        [WRAPPER_SCRIPT, "auth", "status"],
        capture_output=True, text=True, cwd=PROJECT_DIR, env=env
    )
    
    # When session file does NOT exist, the wrapper should leave AMIKA_API_KEY intact.
    assert "Authenticated via AMIKA_API_KEY environment variable" in result.stdout, \
        f"Wrapper script failed to use AMIKA_API_KEY when session file is absent. Output: {result.stdout}"
