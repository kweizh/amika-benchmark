FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika project with an empty directory /home/user/myproject to test mount modes."

RUN mkdir -p /home/user/myproject

# Container contents:
#   - amika installed
#   - docker.io installed to allow amika to communicate with dockerd
#   - /home/user/myproject — an empty project directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
