FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user/project && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Empty environment for installing Amika CLI and configuring authentication."

# Container contents:
#   - Empty /home/user/project directory
#   - Prerequisites for installing Amika CLI (curl, sudo, etc.)

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
