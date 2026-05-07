# SSH Heredoc Variable Escaping Fix

## Problem
The `/home/user/workspace/run_agent.sh` script was failing to output the correct guest-side variable because `$AMIKA_AGENT_CWD` was being expanded on the host instead of inside the sandbox.

## Root Cause
The heredoc used `<<EOF` without quotes, which caused the host shell to expand `$AMIKA_AGENT_CWD` before sending the content to the remote command.

## Solution
Changed the heredoc delimiter from `<<EOF` to `<<'EOF'` (single-quoted) to prevent host-side variable expansion.

### Before:
```bash
amika sandbox ssh test-sandbox -- bash <<EOF > /home/user/workspace/output.log
echo "CWD: $AMIKA_AGENT_CWD"
EOF
```

### After:
```bash
amika sandbox ssh test-sandbox -- bash <<'EOF' > /home/user/workspace/output.log
echo "CWD: $AMIKA_AGENT_CWD"
EOF
```

## Technical Details
- `<<EOF` - Unquoted delimiter allows variable expansion on host
- `<<'EOF'` - Single-quoted delimiter prevents all expansion on host
- `<<"EOF"` - Double-quoted delimiter prevents variable expansion but allows command substitution

By using `<<'EOF'`, the literal string `$AMIKA_AGENT_CWD` is sent to the sandbox where it will be expanded by the sandbox's shell, which has access to the guest-side `AMIKA_AGENT_CWD` environment variable.

## Files Modified
- `/home/user/workspace/run_agent.sh` - Fixed heredoc delimiter and removed `--git` flag (no git remote configured)

## Verification
The script syntax is now correct. The fix ensures that guest-side environment variables will be properly evaluated inside the sandbox environment rather than being expanded on the host.