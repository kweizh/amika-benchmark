FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika workspace with an initialized git repository in /home/user/project for testing SSH heredoc."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    git init && \
    git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    echo "# Amika Heredoc Test" > README.md && \
    git add README.md && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed system-wide via install.sh.
#   - /home/user/project - initialized git repository with a README.md.

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
