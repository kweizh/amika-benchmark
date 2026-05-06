import os
import subprocess
import pytest
import urllib.request
import urllib.error

PROJECT_DIR = "/home/user/project"
LOG_FILE = os.path.join(PROJECT_DIR, "output.log")
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika/config.toml")

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"Config file {CONFIG_FILE} does not exist."
    with open(CONFIG_FILE) as f:
        content = f.read()
    assert "8080" in content, f"Expected port 8080 in {CONFIG_FILE}, got: {content}"

def test_sandbox_service_accessible_via_ssh():
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "service-sandbox", "--", "curl", "-s", "localhost:8080"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh' failed: {result.stderr}"
    assert "Hello Amika" in result.stdout, f"Expected 'Hello Amika' in output, got: {result.stdout}"

def test_output_log_exists_and_contains_url():
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} does not exist."
    with open(LOG_FILE) as f:
        url = f.read().strip()
    
    assert url.startswith("http"), f"Expected a valid URL in {LOG_FILE}, got: {url}"
    
    try:
        response = urllib.request.urlopen(url)
        assert response.status == 200, f"Expected HTTP 200 from {url}, got {response.status}"
        body = response.read().decode('utf-8')
        assert "Hello Amika" in body, f"Expected 'Hello Amika' from public URL, got: {body}"
    except urllib.error.URLError as e:
        pytest.fail(f"Failed to access public URL {url}: {e}")
