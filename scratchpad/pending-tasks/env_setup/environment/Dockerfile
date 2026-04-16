FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    curl -fsSL https://deb.nodesource.com/setup_24.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika sandbox configuration task for a Node.js project."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    git init && \
    cat >package.json <<'EOF'
{
  "name": "myproject",
  "version": "1.0.0",
  "description": "A nodejs project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
EOF

# Container contents:
#   - amika installed via install.sh
#   - Node.js v24 installed
#   - /home/user/myproject initialized as a git repo with a package.json

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
