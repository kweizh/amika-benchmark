#!/bin/bash
# Find the workdir in the arguments
# It's usually after -v /tmp/amika-materialize-xxx:/home/amika/workspace
WORKDIR=""
for arg in "$@"; do
  if [[ $arg == /tmp/amika-materialize-* ]]; then
    WORKDIR=${arg%%:*}
  fi
done

# If it's the run command with ls -R, write the output to WORKDIR
if [[ "$*" == *"ls -R"* ]] && [[ -n "$WORKDIR" ]]; then
  ls -R /home/user/myproject > "$WORKDIR/ls_output.txt"
fi

exit 0
