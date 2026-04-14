FROM ubuntu:24.04

RUN apt-get update && apt-get install -y curl git python3 python3-pip && \
    curl -fsSL https://github.com/jj-vcs/jj/releases/download/v0.38.0/jj-v0.38.0-x86_64-unknown-linux-musl.tar.gz | \
    tar -xz -C /usr/local/bin ./jj && \
    chmod +x /usr/local/bin/jj

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Environment with a complex commit graph."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    git init && \
    jj git init --colocate && \
    jj config set --user user.name "Alice" && \
    jj config set --user user.email "alice@example.com" && \
    echo "Base" > file.txt && jj commit -m "Base commit" && \
    jj bookmark create main && \
    jj new main && \
    jj config set --user user.name "Bob" && \
    echo "Bob 1" > bob1.txt && jj commit -m "Bob 1" && \
    echo "Bob 2" > bob2.txt && jj commit -m "Bob 2" && \
    jj config set --user user.name "Alice" && \
    echo "Alice 1" > alice1.txt && jj commit -m "Alice 1"

# Container contents:
#   - jj installed
#   - /home/user/project with commits by Alice and Bob

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]