import os
import pytest

SCRIPT_PATH = "/home/user/project/run_parallel.sh"

def test_script_exists_and_executable():
    assert os.path.isfile(SCRIPT_PATH), f"Script not found at {SCRIPT_PATH}"
    assert os.access(SCRIPT_PATH, os.X_OK), f"Script at {SCRIPT_PATH} is not executable."

def test_script_creates_sandboxes():
    with open(SCRIPT_PATH) as f:
        content = f.read()
    
    assert "amika sandbox create" in content, "Script does not use 'amika sandbox create'."
    assert "feature-a" in content and "feature-b" in content, "Script does not create 'feature-a' and 'feature-b' sandboxes."
    assert "--git" in content, "Script does not use '--git' flag to create sandboxes."

def test_script_sends_agent_prompts():
    with open(SCRIPT_PATH) as f:
        content = f.read()
    
    assert "amika sandbox agent-send" in content, "Script does not use 'amika sandbox agent-send'."
    assert "Generate frontend components" in content, "Script does not send the prompt to feature-a."
    assert "Generate backend API" in content, "Script does not send the prompt to feature-b."

def test_script_runs_parallel_and_waits():
    with open(SCRIPT_PATH) as f:
        content = f.read()
    
    assert "&" in content, "Script does not run commands in the background using '&'."
    assert "wait" in content, "Script does not use 'wait' to wait for background jobs."
