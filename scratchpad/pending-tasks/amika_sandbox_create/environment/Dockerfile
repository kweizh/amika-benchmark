FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika CLI installed with a git repository in /home/user/workspace."

RUN mkdir -p /home/user/workspace && \
    cd /home/user/workspace && \
    git init && \
    git config user.name "Test User" && \
    git config user.email "test@example.com" && \
    echo "# Test Workspace" > README.md && \
    git add README.md && \
    git commit -m "Initial commit"

# Container contents:
#   - Amika CLI installed.
#   - /home/user/workspace — initialized git repository

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
