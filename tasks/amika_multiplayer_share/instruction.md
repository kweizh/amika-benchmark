# Share Live Preview URL for Multiplayer Debugging

## Background
You have a local git repository at `/home/user/frontend-app` containing a simple frontend application (`index.html`). You want to create a remote sandbox to run this application and share the live preview URL with your teammates.

## Requirements
- Create a remote sandbox named `multiplayer-box` from the git repository at `/home/user/frontend-app`.
- Configure the sandbox to expose port `8080` to the public internet.
- Start a simple HTTP server on port `8080` serving the `index.html` file in the background inside the remote sandbox.
- Retrieve the public URL for the exposed service and save it to `/home/user/frontend-app/share_url.txt`.

## Constraints
- Project path: `/home/user/frontend-app`
- Log file: `/home/user/frontend-app/share_url.txt`
- The sandbox must be named `multiplayer-box`.
- Use Amika CLI to create and manage the sandbox.

## Integrations
- Amika Cloud