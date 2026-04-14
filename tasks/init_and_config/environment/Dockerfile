FROM ubuntu:24.04

RUN apt-get update && apt-get install -y curl git python3 python3-pip && \
    curl -fsSL https://github.com/jj-vcs/jj/releases/download/v0.38.0/jj-v0.38.0-x86_64-unknown-linux-musl.tar.gz | \
    tar -xz -C /usr/local/bin ./jj && \
    chmod +x /usr/local/bin/jj

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Empty environment with jj and git installed."

# Container contents:
#   - jj installed
#   - git installed
#   - /home/user directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]