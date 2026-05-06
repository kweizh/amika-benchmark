#!/bin/bash

# Path to the browser session file
SESSION_FILE="${XDG_STATE_HOME:-$HOME/.local/state}/amika/workos-session.json"

# If the session file exists, unset AMIKA_API_KEY to force amika to use the session
if [ -f "$SESSION_FILE" ]; then
    unset AMIKA_API_KEY
fi

exec amika "$@"
