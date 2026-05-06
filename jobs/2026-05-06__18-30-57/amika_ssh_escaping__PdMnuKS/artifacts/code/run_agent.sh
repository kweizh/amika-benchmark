#!/bin/bash
set -e

# Create a remote sandbox
amika sandbox create --name test-sandbox --git --remote

# Execute a multi-line script inside the sandbox
amika sandbox ssh test-sandbox -- bash <<'EOF' > /home/user/workspace/output.log
echo "CWD: $AMIKA_AGENT_CWD"
EOF
