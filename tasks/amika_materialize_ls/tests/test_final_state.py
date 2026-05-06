import os
import pytest

LOGS_DIR = "/home/user/logs"

def test_logs_dir_exists():
    assert os.path.isdir(LOGS_DIR), f"Logs directory {LOGS_DIR} does not exist."

def test_logs_dir_not_empty():
    files = os.listdir(LOGS_DIR)
    assert len(files) > 0, f"Logs directory {LOGS_DIR} is empty, expected output files from amika materialize."
