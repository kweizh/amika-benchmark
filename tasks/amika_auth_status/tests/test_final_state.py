import os
import subprocess
import pytest

LOG_FILE = "/home/user/output.log"

def test_output_log_exists():
    assert os.path.isfile(LOG_FILE), f"The output log file was not found at {LOG_FILE}."

def test_output_log_content():
    # Run the command to get the expected output
    result = subprocess.run(
        ["amika", "auth", "status"],
        capture_output=True,
        text=True,
        cwd="/home/user"
    )
    
    # The output might be in stdout or stderr depending on whether it succeeded or failed
    expected_output = result.stdout.strip()
    if not expected_output:
        expected_output = result.stderr.strip()
        
    with open(LOG_FILE, "r") as f:
        actual_content = f.read().strip()
        
    # Check if the content matches or contains the expected output
    assert actual_content != "", "The output log file is empty."
    
    # Since the agent might have redirected both stdout and stderr, or added formatting, 
    # we check if the core part of the expected output is in the file.
    # If the command failed due to auth, the error message should be present.
    if expected_output:
        # Just check if a significant part of the output is in the log file
        # We'll take the first line of the expected output to avoid exact whitespace matching issues
        first_line = expected_output.split('\n')[0].strip()
        assert first_line in actual_content, f"Expected output '{first_line}' not found in {LOG_FILE}. Actual content: {actual_content}"
