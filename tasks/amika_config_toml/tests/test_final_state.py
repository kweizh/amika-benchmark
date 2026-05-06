import os
import tomllib
import pytest

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika", "config.toml")

def test_config_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(CONFIG_FILE), \
        f".amika/config.toml not found at {CONFIG_FILE}"

def test_config_contents():
    """Priority 3 fallback: check config.toml contents."""
    with open(CONFIG_FILE, "rb") as f:
        try:
            config = tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            pytest.fail(f"Failed to parse TOML file: {e}")

    # Verify lifecycle.setup_script
    assert "lifecycle" in config, "Missing [lifecycle] section in config.toml"
    assert config["lifecycle"].get("setup_script") == "scripts/setup.sh", \
        f"Expected lifecycle.setup_script to be 'scripts/setup.sh', got: {config['lifecycle'].get('setup_script')}"

    # Verify env.NODE_ENV
    assert "env" in config, "Missing [env] section in config.toml"
    assert config["env"].get("NODE_ENV") == "development", \
        f"Expected env.NODE_ENV to be 'development', got: {config['env'].get('NODE_ENV')}"

    # Verify services.web
    assert "services" in config, "Missing [services] section in config.toml"
    assert "web" in config["services"], "Missing [services.web] section in config.toml"
    assert config["services"]["web"].get("port") == 3000, \
        f"Expected services.web.port to be 3000, got: {config['services']['web'].get('port')}"
    assert config["services"]["web"].get("url_scheme") == "http", \
        f"Expected services.web.url_scheme to be 'http', got: {config['services']['web'].get('url_scheme')}"

    # Verify sandbox.preset
    assert "sandbox" in config, "Missing [sandbox] section in config.toml"
    assert config["sandbox"].get("preset") == "coder", \
        f"Expected sandbox.preset to be 'coder', got: {config['sandbox'].get('preset')}"
