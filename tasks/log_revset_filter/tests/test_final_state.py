import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/repo"
RESULT_FILE = "/home/user/result.txt"

def test_result_file_exists():
    assert os.path.isfile(RESULT_FILE), f"The output file {RESULT_FILE} was not created."

def test_result_content_matches_expected():
    # Run jj log to get the expected output
    result = subprocess.run(
        ["jj", "log", "-r", "author(\"Bob\") & main..@", "-T", "change_id.short() ++ \"\\n\""],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "Failed to run jj log to determine the expected output."
    expected_output = result.stdout.strip().splitlines()
    
    # Read the actual output
    with open(RESULT_FILE, "r") as f:
        actual_output = f.read().strip().splitlines()
        
    assert len(actual_output) > 0, f"The output file {RESULT_FILE} is empty."
    
    # Sort both lists to compare the sets of change IDs, as order might vary depending on the exact query execution
    expected_output_sorted = sorted(expected_output)
    actual_output_sorted = sorted(actual_output)
    
    assert actual_output_sorted == expected_output_sorted, (
        f"The change IDs in {RESULT_FILE} do not match the expected ones. "
        f"Expected: {expected_output_sorted}, Got: {actual_output_sorted}"
    )
