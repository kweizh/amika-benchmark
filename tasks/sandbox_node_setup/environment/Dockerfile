FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    curl -fsSL https://deb.nodesource.com/setup_24.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Node.js project environment for Amika sandbox setup."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    git init && \
    git config --global user.email "test@example.com" && \
    git config --global user.name "Test User" && \
    cat >package.json <<'EOF'
{
  "name": "project",
  "version": "1.0.0",
  "description": "A simple Node.js project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
EOF
RUN cd /home/user/project && \
    cat >index.js <<'EOF'
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello World!'));
app.listen(3000, () => console.log('Listening on port 3000'));
EOF
RUN cd /home/user/project && \
    git add package.json index.js && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed
#   - docker.io installed
#   - nodejs installed
#   - /home/user/project - Node.js project with package.json

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
