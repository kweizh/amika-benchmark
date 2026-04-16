import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_amika_not_installed():
    assert shutil.which("amika") is None, "amika binary should not exist before the task."

def test_config_dir_does_not_exist():
    config_dir = "/root/.config/amika"
    assert not os.path.exists(config_dir), f"Config directory {config_dir} should not exist before the task."
