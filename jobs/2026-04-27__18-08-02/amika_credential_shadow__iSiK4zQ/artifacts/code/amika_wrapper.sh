#!/bin/bash

# Determine the session file path
SESSION_FILE="${XDG_STATE_HOME:-$HOME/.local/state}/amika/workos-session.json"

# Check if the session file exists
if [ -f "$SESSION_FILE" ]; then
    # Unset AMIKA_API_KEY so amika uses the browser session
    unset AMIKA_API_KEY
fi

# Execute amika with original arguments
amika "$@"
