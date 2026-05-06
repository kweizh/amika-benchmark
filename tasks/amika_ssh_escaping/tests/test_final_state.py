import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/workspace"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "run_agent.sh")
LOG_FILE = os.path.join(PROJECT_DIR, "output.log")

def test_script_execution():
    """Priority 1: Run the script and verify it succeeds."""
    result = subprocess.run(["bash", "run_agent.sh"], cwd=PROJECT_DIR, capture_output=True, text=True)
    assert result.returncode == 0, f"Script execution failed: {result.stderr}"

def test_log_file_contains_correct_cwd():
    """Priority 3: Verify the log file contains the guest-side CWD."""
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} was not created."
    with open(LOG_FILE) as f:
        content = f.read().strip()
    
    # If the variable was evaluated on the host, it would be empty (or host's value).
    # The expected guest-side CWD should be a non-empty path, likely /workspace or /home/user/workspace.
    # We check that it's not just "CWD: "
    assert "CWD: /" in content, f"Expected log file to contain a valid path, got: {content}"
    assert "CWD: \n" not in content and content != "CWD:", "Variable was likely evaluated on the host (empty)."

def test_script_content_fixed():
    """Priority 3: Verify the script was actually modified to fix the escaping issue."""
    with open(SCRIPT_PATH) as f:
        content = f.read()
    
    # Check if either the variable is escaped \$AMIKA_AGENT_CWD or the heredoc is quoted <<'EOF' or <<"EOF"
    is_escaped_var = r'\$AMIKA_AGENT_CWD' in content
    is_quoted_heredoc = "<<'EOF'" in content or '<<"EOF"' in content
    
    assert is_escaped_var or is_quoted_heredoc, \
        "Script does not contain escaped variable (\\$AMIKA_AGENT_CWD) or quoted heredoc (<<'EOF')."
