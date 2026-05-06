FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    curl -fsSL https://deb.nodesource.com/setup_24.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with a Node.js web server listening on port 8080."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >server.js <<'EOF'
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Amika\n');
});
server.listen(8080, () => {
  console.log('Server listening on port 8080');
});
EOF

# Container contents:
#   - always required libs: curl ca-certificates git python3 python3-pip python3-pytest bash
#   - Node.js v24 installed
#   - amika CLI installed
#   - /home/user/project: base directory for the project with server.js

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
