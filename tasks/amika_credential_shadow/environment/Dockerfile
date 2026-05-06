FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika wrapper script for credential shadowing task."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >amika_wrapper.sh <<'EOF'
#!/bin/bash
amika "$@"
EOF

RUN chmod +x /home/user/project/amika_wrapper.sh

# Container contents:
#   - amika installed system-wide
#   - /home/user/project: project directory
#   - /home/user/project/amika_wrapper.sh: initial wrapper script

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]