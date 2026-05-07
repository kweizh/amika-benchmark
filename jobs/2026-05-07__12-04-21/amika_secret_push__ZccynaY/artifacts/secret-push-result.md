# Amika Secret Push — Result

## Command Executed

```bash
cd /home/user/amika-project && echo "y" | amika secret push mock-key=sk-ant-api03-mock-key-123
```

## Output

```
SECRET    VALUE
mock-key  sk-a*****************-123

Push 1 secret(s) to remote store? [y/N]   Updated mock-key

Pushed 1 secret(s).
```

## Details

| Field       | Value                        |
|-------------|------------------------------|
| Secret name | `mock-key`                   |
| Secret type | `api_key` (Claude API key)   |
| Value       | `sk-ant-api03-mock-key-123`  |
| Scope       | `user` (default / private)   |
| Status      | ✅ Pushed successfully        |
