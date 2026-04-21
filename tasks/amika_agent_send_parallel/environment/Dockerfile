FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika task environment with a git repository initialized in /home/user/myproject."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    git init && \
    git config user.email "test@example.com" && \
    git config user.name "Test User" && \
    echo "# My Project" > README.md && \
    git add README.md && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed system-wide
#   - /home/user/myproject  — initialized git repository

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
