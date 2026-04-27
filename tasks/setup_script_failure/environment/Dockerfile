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
LABEL Description="Node.js project configured with Amika sandbox with a failing setup_script."

RUN mkdir -p /workspace/project && \
    cd /workspace/project && \
    git init && \
    git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    cat >package.json <<'EOF'
{
  "name": "project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
EOF
RUN cd /workspace/project && \
    cat >index.js <<'EOF'
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello World!'));
app.listen(3000, () => console.log('Server ready on port 3000'));
EOF
RUN cd /workspace/project && \
    mkdir -p .amika && \
    cat >.amika/config.toml <<'EOF'
[lifecycle]
setup_script = "npm isntall"

[services.web]
port = 3000
EOF
RUN cd /workspace/project && \
    git add . && \
    git commit -m "Initial commit"

# Container contents:
#   - amika CLI installed
#   - Node.js v24 installed
#   - /workspace/project with a Node.js app and .amika/config.toml containing a typo in setup_script

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]