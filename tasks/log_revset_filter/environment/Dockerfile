FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://github.com/jj-vcs/jj/releases/download/v0.38.0/jj-v0.38.0-x86_64-unknown-linux-musl.tar.gz | \
    tar -xz -C /usr/local/bin ./jj && \
    chmod +x /usr/local/bin/jj

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Jujutsu repository with a specific commit history authored by multiple users."

RUN mkdir -p /home/user/repo && \
    cd /home/user/repo && \
    jj config set --user user.name "Alice" && \
    jj config set --user user.email "alice@example.com" && \
    jj git init . && \
    echo "initial" > file.txt && \
    jj commit -m "initial commit" && \
    jj bookmark create main && \
    jj config set --user user.name "Bob" && \
    jj config set --user user.email "bob@example.com" && \
    echo "bob update 1" >> file.txt && \
    jj commit -m "bob update 1" && \
    jj config set --user user.name "Alice" && \
    jj config set --user user.email "alice@example.com" && \
    echo "alice update" >> file.txt && \
    jj commit -m "alice update" && \
    jj config set --user user.name "Bob" && \
    jj config set --user user.email "bob@example.com" && \
    echo "bob update 2" >> file.txt && \
    jj commit -m "bob update 2" && \
    jj config set --user user.name "Charlie" && \
    jj config set --user user.email "charlie@example.com" && \
    echo "charlie update" >> file.txt

# Container contents:
#   - jj installed for jj log revset filter task.
#   - /home/user/repo - initialized jj repository with main bookmark and commits by Bob, Alice, and Charlie.

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]