FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with a git repository containing multiple branches with different configuration."

RUN git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    git init -b main && \
    mkdir -p .amika && \
    echo '[env]\nTEST_VAR = "main-value"' > .amika/config.toml && \
    git add .amika/config.toml && \
    git commit -m "Initial commit on main" && \
    git checkout -b feature-env && \
    echo '[env]\nTEST_VAR = "feature-value"' > .amika/config.toml && \
    git add .amika/config.toml && \
    git commit -m "Update TEST_VAR on feature-env" && \
    git checkout main

# Container contents:
#   - docker, amika installed
#   - /home/user/myproject - git repository with main and feature-env branches
#   - .amika/config.toml configured with different env variables on each branch

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
