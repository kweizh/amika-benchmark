FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project initialized with a git repository and a benchmark-branch."

RUN git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    mkdir -p /home/user/repo && \
    cd /home/user/repo && \
    git init -b main && \
    echo "initial" > README.md && \
    git add README.md && \
    git commit -m "Initial commit" && \
    git checkout -b benchmark-branch && \
    echo "benchmark" > benchmark.txt && \
    git add benchmark.txt && \
    git commit -m "Add benchmark file" && \
    git checkout main

# Container contents:
#   - amika installed
#   - /home/user/repo initialized as git repository with benchmark-branch

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
