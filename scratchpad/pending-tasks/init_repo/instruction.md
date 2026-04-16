# Initialize Amika Repository

## Background
Amika uses a declarative `.amika/config.toml` file at the root of a git repository to define sandbox configurations. You need to create this file to configure the environment lifecycle.

## Requirements
- Create a `.amika/config.toml` file at the root of the existing git repository located at `/home/user/myproject`.
- The configuration file should contain a `[lifecycle]` section with `setup_script` set to `"npm install"`.

## Implementation Guide
1. Navigate to `/home/user/myproject`.
2. Create the `.amika` directory.
3. Create the `config.toml` file inside `.amika` with the required content.

## Constraints
- Project path: /home/user/myproject