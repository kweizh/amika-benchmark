FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project environment with amika CLI installed."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    git init && \
    echo 'if [ -n "$AMIKA_API_KEY" ]; then echo "$AMIKA_API_KEY" | amika auth login --api-key-file - > /dev/null 2>&1 || true; fi' >> /home/user/.bashrc

# Container contents:
#   - amika installed for amika project.
#   - /home/user/myproject  — amika project initialized with git
#   - auto-authentication logic in .bashrc if AMIKA_API_KEY is provided

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]