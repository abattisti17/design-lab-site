# design-lab-site

Source for designlab.fyi (Design Strategy Lab LLC).

- Site files live in `designlab_html/`.
- Every push to `main` that touches `designlab_html/` uploads it to Electric Embers (`/home/<user>/designlab_html`) via GitHub Actions.
- To redeploy without a change: Actions tab > "Deploy to Electric Embers" > Run workflow.
- Deploys only upload. Deleting a file here does not delete it on the server.

Required repo secrets: `SFTP_HOST`, `SFTP_USERNAME`, `SFTP_PASSWORD`, `SFTP_PATH`.

## Checks and deploys

`.github/workflows/deploy.yml` runs on every pull request and every push to `main`:

1. **Checks:** HTML validation, internal link check, and screenshots of every page at phone and desktop widths. A page that scrolls sideways or logs a console error fails the run. Screenshots are attached to each run under "Artifacts".
2. **Staging (pull requests):** uploads to the staging site if the `STAGING_SFTP_PATH` secret is set. Staging gets a `robots.txt` that blocks search engines.
3. **Production (push to `main`):** uploads to designlab.fyi, only if the checks passed.
