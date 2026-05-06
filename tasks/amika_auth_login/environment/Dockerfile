FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Amika task environment with a mock API key file."

RUN echo "amk_mock_key_12345" > /home/user/amika_key.txt && \
    chmod 0600 /home/user/amika_key.txt && \
    chown -R root:root /home/user

# Container contents:
#   - amika CLI installed
#   - /home/user/amika_key.txt with a mock API key

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
