import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/workspace"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "run_agent.sh")

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_run_agent_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script {SCRIPT_PATH} does not exist."

def test_initial_script_content():
    with open(SCRIPT_PATH) as f:
        content = f.read()
    assert 'echo "CWD: $AMIKA_AGENT_CWD"' in content, "Expected initial script to contain unescaped $AMIKA_AGENT_CWD"
    assert '<<EOF' in content, "Expected initial script to use unquoted heredoc <<EOF"
