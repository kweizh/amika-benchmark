FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika environment for materializing large outputs."

RUN mkdir -p /home/user/project

# Container contents:
#   - amika installed.
#   - /home/user/project  — empty project directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
