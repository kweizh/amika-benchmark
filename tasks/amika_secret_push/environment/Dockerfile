FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project environment for pushing a secret."

RUN mkdir -p /home/user/amika-project

# Container contents:
#   - amika CLI installed.
#   - /home/user/amika-project  — project directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
