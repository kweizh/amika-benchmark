FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with an initial TOML config defining API_TOKEN."

RUN git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    mkdir -p /home/user/myproject/.amika && \
    cd /home/user/myproject && \
    git init && \
    cat >.amika/config.toml <<'EOF'
[env]
API_TOKEN = "toml_default_token"
EOF

RUN cd /home/user/myproject && \
    git add .amika/config.toml && \
    git commit -m "Initial commit"

# Container contents:
#   - amika CLI installed
#   - /home/user/myproject — git repository with .amika/config.toml defining API_TOKEN

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
