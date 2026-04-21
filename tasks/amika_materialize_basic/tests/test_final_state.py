import os
import json
import pytest

WORKSPACE_DIR = "/workspace"
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "output", "report.json")

def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), f"Expected output file {OUTPUT_FILE} does not exist."

def test_output_file_content():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read().strip()
    
    # Check exact string match as requested by the task
    assert content == '{"status": "success"}', f"Expected file content to be '{{\"status\": \"success\"}}', but got: {content}"

    # Also verify it's valid JSON
    try:
        data = json.loads(content)
        assert data.get("status") == "success", "JSON parsed successfully but 'status' is not 'success'."
    except json.JSONDecodeError:
        pytest.fail(f"Content in {OUTPUT_FILE} is not valid JSON.")
