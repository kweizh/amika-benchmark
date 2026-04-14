# Initialize and Configure Jujutsu

## Background
Jujutsu (`jj`) is a modern, Git-compatible version control system. You need to initialize a new repository and set up your user identity.

## Requirements
- Initialize a new Git-colocated `jj` repository in the project directory.
- Configure the user name as "Alice Developer".
- Configure the user email as "alice@example.com".

## Implementation
1. Navigate to `/home/user/project`.
2. Initialize the repository using `jj git init --colocate`.
3. Set the user name using `jj config set --user user.name "Alice Developer"`.
4. Set the user email using `jj config set --user user.email "alice@example.com"`.

## Constraints
- Project path: `/home/user/project`
- Start command: none
- Port: none