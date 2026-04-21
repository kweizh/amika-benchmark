FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with a port collision in .amika/config.toml."

RUN mkdir -p /home/user/myproject/.amika && \
    cd /home/user/myproject && \
    cat >.amika/config.toml <<'EOF'
[services.frontend]
port = 3000
host_port = 3000

[services.api]
port = 8080
host_port = 3000
EOF

# Container contents:
#   - amika installed
#   - /home/user/myproject  — Amika project with initial config
#   - .amika/config.toml with port collision on host_port = 3000

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]