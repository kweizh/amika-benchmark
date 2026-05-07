#!/bin/bash
set -e

# Create a remote sandbox
amika sandbox create --name test-sandbox --git --remote || true

# Execute a multi-line script inside the sandbox
amika sandbox ssh test-sandbox --remote -- bash <<'EOF' > /home/user/workspace/output.log
echo "CWD: $AMIKA_AGENT_CWD"
EOF
