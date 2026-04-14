# Jujutsu Alias Configuration

## Background
Jujutsu (`jj`) allows you to define command aliases to simplify your workflow. You can configure these globally for your user.

## Requirements
1. Initialize a new `jj` repository collocated with git in `/home/user/myproject`.
2. Configure the `jj` user name as "Test User" and email as "test@example.com".
3. Configure a user-level `jj` alias named `mylog` that translates to `log -r @-`.
4. Create a file `hello.txt` with the content `Hello jj` in the project.
5. Record the change by creating a new commit with the message `Add hello.txt` (e.g., using `jj new -m "Add hello.txt"` or `jj commit -m "Add hello.txt"`).

## Constraints
- Project path: `/home/user/myproject`
- The alias must be a user-level configuration (using `jj config set --user`).
- The alias `mylog` should execute `log` with the arguments `-r` and `@-`.