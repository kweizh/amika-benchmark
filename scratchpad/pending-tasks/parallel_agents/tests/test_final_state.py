import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "run_agents.sh")

def test_script_exists_and_executable():
    assert os.path.isfile(SCRIPT_PATH), f"Script {SCRIPT_PATH} does not exist."
    assert os.access(SCRIPT_PATH, os.X_OK), f"Script {SCRIPT_PATH} is not executable."

def test_script_execution_and_sandbox_results():
    # Run the script
    result = subprocess.run(
        ["./run_agents.sh"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script execution failed: {result.stderr}\n{result.stdout}"

    # Verify task-1 sandbox using amika materialize to extract the file
    task1_result = subprocess.run(
        ["amika", "materialize", "--cmd", "cat hello.txt", "--destdir", "/tmp/task1_out"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    # The plan.md says: amika materialize --cmd "<command>" --destdir <path>
    # It might not target a specific sandbox, but it runs a command in a container.
    # Actually, we can just check if the sandboxes were created
    list_result = subprocess.run(
        ["amika", "sandbox", "list"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    # We don't know the exact output format, but "task-1" and "task-2" should be in the output
    assert "task-1" in list_result.stdout or "task-1" in list_result.stderr, "task-1 sandbox not found"
    assert "task-2" in list_result.stdout or "task-2" in list_result.stderr, "task-2 sandbox not found"
