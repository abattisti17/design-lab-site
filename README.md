# design-lab-site

Source for designlab.fyi (Design Strategy Lab LLC).

- Site files live in `designlab_html/`.
- Every push to `main` that touches `designlab_html/` uploads it to Electric Embers (`/home/<user>/designlab_html`) via GitHub Actions.
- To redeploy without a change: Actions tab > "Deploy to Electric Embers" > Run workflow.
- Deploys only upload. Deleting a file here does not delete it on the server.

Required repo secrets: `SFTP_HOST`, `SFTP_USERNAME`, `SFTP_PASSWORD`, `SFTP_PATH`.
