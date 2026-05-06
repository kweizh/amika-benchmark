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
LABEL Description="Amika environment with a Node.js project at /home/user/myproject."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    npm init -y

# Container contents:
#   - amika installed
#   - Node.js v24 installed
#   - /home/user/myproject: initialized Node.js project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
