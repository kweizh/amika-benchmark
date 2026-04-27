FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with an initial failing setup script in /home/user/project."

RUN mkdir -p /home/user/project/.amika && \
    cd /home/user/project && \
    git init && \
    git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    cat >.amika/config.toml <<'EOF'
[lifecycle]
setup_script = ".amika/setup.sh"
EOF
    
RUN cd /home/user/project && \
    cat >.amika/setup.sh <<'EOF'
#!/bin/bash
echo "Running setup..."
exit 1
EOF
    
RUN cd /home/user/project && \
    git add . && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed for amika project.
#   - /home/user/project  — amika project initialized as git repository
#   - .amika/config.toml with setup_script configured
#   - .amika/setup.sh which fails (exits with 1) and is not executable

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
