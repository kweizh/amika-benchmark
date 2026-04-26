#!/bin/bash
echo "Arguments: $@" >> /tmp/docker_args
if [[ "$@" == *"inspect"* ]]; then
  echo "[]"
elif [[ "$@" == *"run"* ]]; then
  echo "abcdef1234567890"
fi
exit 0
