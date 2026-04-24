#!/bin/bash

# Create the sandbox with the specified mount and rw mode
amika sandbox create --name dev-sandbox --mount /home/user/myproject:/workspace/myproject:rw --yes

# Run the command inside the sandbox to create the output file
amika sandbox ssh dev-sandbox -- "echo 'hello from sandbox' > /workspace/myproject/output.txt"
