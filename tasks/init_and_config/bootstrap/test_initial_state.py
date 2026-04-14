import os
import shutil
import pytest

def test_jj_binary_available():
    assert shutil.which("jj") is not None, "jj binary not found in PATH."

def test_git_binary_available():
    assert shutil.which("git") is not None, "git binary not found in PATH."
