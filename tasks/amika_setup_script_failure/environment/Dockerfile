FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with a failing setup script."

RUN mkdir -p /home/user/myproject/.amika && \
    cd /home/user/myproject && \
    git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    git init && \
    cat >.amika/config.toml <<'EOF'
[lifecycle]
setup_script = "./setup.sh"
EOF
RUN cd /home/user/myproject && \
    cat >setup.sh <<'EOF'
#!/bin/bash
echo "Setting up..."
exit 1
EOF
RUN cd /home/user/myproject && \
    chmod +x setup.sh && \
    git add . && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed
#   - /home/user/myproject initialized as a git repo
#   - .amika/config.toml with a failing setup_script

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
