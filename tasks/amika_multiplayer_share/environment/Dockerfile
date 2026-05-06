FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with a local git repository containing an index.html file."

RUN mkdir -p /home/user/frontend-app && \
    cd /home/user/frontend-app && \
    git init && \
    echo "Hello from frontend" > index.html && \
    git add index.html && \
    git config user.name "Test User" && \
    git config user.email "test@example.com" && \
    git commit -m "Initial commit"

# Container contents:
#   - amika installed
#   - /home/user/frontend-app  — local git repository with index.html

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
