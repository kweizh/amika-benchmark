FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash sudo docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika sandbox creation task environment with a pre-initialized git repository."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    git config --global user.name "Test User" && \
    git config --global user.email "test@example.com" && \
    git init && \
    echo "# My Project" > README.md && \
    git add README.md && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed system-wide.
#   - docker.io installed to allow local sandbox creation.
#   - /home/user/myproject - a git repository for the project.

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
