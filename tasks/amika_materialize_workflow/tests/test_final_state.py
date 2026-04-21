import os
import json
import pytest

OUTPUT_DIR = "/home/user/workspace/output"
REPORT_FILE = os.path.join(OUTPUT_DIR, "report.json")

def test_report_json_exists():
    """Verify that report.json was created in the correct directory."""
    assert os.path.isfile(REPORT_FILE), f"Expected {REPORT_FILE} to exist, but it was not found."

def test_report_json_content():
    """Verify the contents of report.json."""
    with open(REPORT_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(f"Failed to parse {REPORT_FILE} as JSON: {e}")

    assert data.get("status") == "success", f"Expected 'status' to be 'success', got: {data.get('status')}"
    assert data.get("data") == "materialized", f"Expected 'data' to be 'materialized', got: {data.get('data')}"
