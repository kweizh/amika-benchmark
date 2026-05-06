FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika workspace with a script that has a heredoc variable escaping bug."

RUN mkdir -p /home/user/workspace && \
    cd /home/user/workspace && \
    git init && \
    git branch -M main && \
    cat > run_agent.sh <<'SCRIPT'
#!/bin/bash
set -e

# Create a remote sandbox
amika sandbox create --name test-sandbox --git --remote

# Execute a multi-line script inside the sandbox
amika sandbox ssh test-sandbox -- bash <<EOF > /home/user/workspace/output.log
echo "CWD: $AMIKA_AGENT_CWD"
EOF
SCRIPT
RUN cd /home/user/workspace && \
    chmod +x run_agent.sh && \
    git add run_agent.sh && \
    git config user.email "test@example.com" && \
    git config user.name "Test User" && \
    git commit -m "Initial commit"

# Container contents:
#   - amika CLI installed.
#   - /home/user/workspace - Git repository containing run_agent.sh with unescaped heredoc variable.

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
