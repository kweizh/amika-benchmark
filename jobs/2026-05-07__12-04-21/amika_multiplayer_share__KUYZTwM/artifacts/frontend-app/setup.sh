#!/bin/bash
# Create the workspace directory and index.html
mkdir -p /home/amika/workspace/frontend-app
echo 'Hello from frontend' > /home/amika/workspace/frontend-app/index.html

# Start HTTP server on port 8080 in the background
cd /home/amika/workspace/frontend-app
nohup python3 -m http.server 8080 > /tmp/httpserver.log 2>&1 &
echo "HTTP server started with PID $!"
