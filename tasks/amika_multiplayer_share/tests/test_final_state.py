import os
import subprocess
import json
import urllib.request
import pytest

PROJECT_DIR = "/home/user/frontend-app"
SHARE_URL_FILE = os.path.join(PROJECT_DIR, "share_url.txt")

def test_sandbox_running_via_cli():
    """Priority 1: Use Amika CLI to verify the sandbox state."""
    result = subprocess.run(
        ["amika", "sandbox", "list", "--remote"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "multiplayer-box" in result.stdout, f"Expected 'multiplayer-box' in running sandboxes, got: {result.stdout}"

def test_service_exposed_via_cli():
    """Priority 1: Use Amika CLI to verify the exposed service."""
    result = subprocess.run(
        ["amika", "service", "list", "--sandbox-name", "multiplayer-box"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika service list' failed: {result.stderr}"
    assert "8080" in result.stdout, f"Expected port 8080 to be exposed, got: {result.stdout}"

def test_share_url_file_exists_and_valid():
    """Priority 3: Verify the output file contains a valid URL."""
    assert os.path.isfile(SHARE_URL_FILE), f"share_url.txt not found at {SHARE_URL_FILE}"
    with open(SHARE_URL_FILE, "r") as f:
        url = f.read().strip()
    
    assert url.startswith("http://") or url.startswith("https://"), f"Invalid URL format in {SHARE_URL_FILE}: {url}"
    
    # Verify the URL is accessible and returns the expected content
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode("utf-8")
        assert response.status == 200, f"Expected HTTP 200, got {response.status}"
        assert "Hello from frontend" in content, f"Expected 'Hello from frontend' in response, got: {content}"
    except Exception as e:
        pytest.fail(f"Failed to access URL {url}: {e}")
