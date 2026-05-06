FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika materialize environment with a data processing script."

RUN mkdir -p /home/user/app && \
    cd /home/user/app && \
    cat >process.sh <<'EOF'
#!/bin/bash
mkdir -p /logs
echo "Processing complete" > /logs/output.log
EOF
RUN chmod +x /home/user/app/process.sh

# Container contents:
#   - amika installed
#   - /home/user/app  — project directory
#   - process.sh — data processing script

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
