FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user && \
    mkdir -p /workspace && chmod 0777 /workspace

LABEL Author="any-task-builder"
LABEL Description="Amika materialization basic task environment"

# Container contents:
#   - amika installed via install.sh
#   - docker.io installed for amika to interact with docker
#   - /workspace directory created for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
