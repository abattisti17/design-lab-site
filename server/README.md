# Sign-up database

Every door page posts to `designlab_html/join/submit.php`. It saves one row per sign-up in a table called `signups`, in a SQLite file (`signups.db`) that it creates on the first sign-up. MySQL also works; see `config.example.php`.

## One-time setup

1. In Cyberduck (SFTP, port 22212), make a folder called `designlab-private` next to `designlab_html`, not inside it.
2. Upload `config.example.php` into that folder, renamed to `config.php`. No edits needed for SQLite.
3. Visit any door page and sign up with your own email. You should land on the thanks page, and `signups.db` should appear in the folder.

## Columns

- `email`, `created_at` (UTC)
- `page`: which door (billing, records, construction, new-work, benchmarks)
- `cohort`: who the page is for (architecture)
- `test`: which round of tests (door-v1)
- `variant`: page version, for A/B tests later (a)
- `source`, `medium`, `campaign`: from `utm_` tags on the link, if any
- `ref_host`: the site they came from (for example google.com), host only
- `landing`: the page path
- `status`: starts as `new`. Change it by hand (contacted, called, deposit)
- `notes`: free text

No IP addresses or browser details are stored.

## Viewing sign-ups

Download `signups.db` with Cyberduck and open it in DB Browser for SQLite (free), which can export CSV for Numbers.
