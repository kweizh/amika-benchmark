FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika full-stack project environment with an intentional port conflict and missing environment variables."

RUN mkdir -p /home/user/myproject/.amika && \
    mkdir -p /home/user/myproject/frontend && \
    mkdir -p /home/user/myproject/api && \
    cd /home/user/myproject && \
    cat >.amika/config.toml <<'EOF'
[lifecycle]
setup_script = "echo 'Setting up...' && if [ -z \"$DB_PASSWORD\" ]; then echo 'Missing DB_PASSWORD'; exit 1; fi; echo 'Done'"

[env]
NODE_ENV = "development"

[services.frontend]
port = "3000:3000"

[services.api]
port = "3000:8080"
EOF

RUN cat >/home/user/myproject/frontend/.env <<'EOF'
REACT_APP_API_URL=http://localhost:3000
EOF

# Container contents:
#   - amika installed system-wide.
#   - /home/user/myproject - project with an intentional port conflict in config.toml
#   - /home/user/myproject/frontend/.env - frontend config pointing to the conflicting port

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]