#!/bin/bash
# Amika authentication wrapper script
# Reads API key from /home/user/amika_key.txt and authenticates

export AMIKA_API_KEY=$(cat /home/user/amika_key.txt)
exec amika "$@"