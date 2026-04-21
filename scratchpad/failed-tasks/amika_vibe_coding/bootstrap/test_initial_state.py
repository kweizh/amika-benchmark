import os
import shutil
import pytest

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_git_binary_available():
    assert shutil.which("git") is not None, "git binary not found in PATH."

def test_docker_binary_available():
    assert shutil.which("docker") is not None, "docker binary not found in PATH."
