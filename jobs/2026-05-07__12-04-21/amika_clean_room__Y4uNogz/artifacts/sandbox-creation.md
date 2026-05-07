# Amika Sandbox Creation — my-benchmark-box

## Command Used

```bash
cd /home/user/repo
amika sandbox create --remote \
  --name my-benchmark-box \
  --git \
  --branch benchmark-branch
```

## Result

| Field    | Value              |
|----------|--------------------|
| Name     | my-benchmark-box   |
| State    | stopped            |
| Location | remote             |
| Provider | daytona            |
| Branch   | benchmark-branch   |
| Created  | 2026-05-07T03:13:55.792Z |

## Notes

- `--remote` targets the remote Daytona provider instead of local Docker.
- `--git` (no argument) instructs the CLI to auto-detect the git root from the current working directory and resolve the `origin` remote URL for cloning.
- `--branch benchmark-branch` pins the sandbox to the `benchmark-branch` branch.
- `AMIKA_API_KEY` was already set in the environment; no explicit auth flags were required.
