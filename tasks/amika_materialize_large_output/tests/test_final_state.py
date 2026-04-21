import os
import json
import pytest

PROJECT_DIR = "/home/user/project"

def test_generate_script_exists():
    script_path = os.path.join(PROJECT_DIR, "generate.py")
    assert os.path.isfile(script_path), f"generate.py not found at {script_path}"

def test_output_log_exists():
    log_path = os.path.join(PROJECT_DIR, "output.log")
    assert os.path.isfile(log_path), f"output.log not found at {log_path}"

def test_output_directory_exists():
    output_dir = os.path.join(PROJECT_DIR, "output")
    assert os.path.isdir(output_dir), f"Output directory not found at {output_dir}"

def test_report_json_exists():
    report_path = os.path.join(PROJECT_DIR, "output", "report.json")
    assert os.path.isfile(report_path), f"report.json not found at {report_path}"

def test_report_json_content():
    report_path = os.path.join(PROJECT_DIR, "output", "report.json")
    try:
        with open(report_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        pytest.fail(f"Failed to parse report.json: {e}")
    except Exception as e:
        pytest.fail(f"Failed to read report.json: {e}")

    assert isinstance(data, list), f"Expected report.json to contain a JSON array, got {type(data)}"
    assert len(data) == 10000, f"Expected report.json to contain exactly 10,000 items, got {len(data)}"
    
    last_item = data[-1]
    assert "id" in last_item, "Expected 'id' in the last item"
    assert last_item["id"] == 10000, f"Expected last item 'id' to be 10000, got {last_item['id']}"
    assert "timestamp" in last_item, "Expected 'timestamp' in the last item"
