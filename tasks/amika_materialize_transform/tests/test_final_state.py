import os
import json
import pytest

PROJECT_DIR = "/home/user/project"
OUTPUT_FILE = os.path.join(PROJECT_DIR, "results", "output.json")

def test_output_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(OUTPUT_FILE), f"Output file not found at {OUTPUT_FILE}"

def test_output_file_contents():
    """Priority 3 fallback: file content check."""
    with open(OUTPUT_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"Failed to parse {OUTPUT_FILE} as JSON.")
    
    expected = [1, 4, 9, 16, 25]
    assert data == expected, f"Expected {expected}, got {data}"
