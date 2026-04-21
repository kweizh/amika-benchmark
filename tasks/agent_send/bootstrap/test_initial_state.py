import os
import shutil
import subprocess
import pytest

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."
