# Sign-up database

Every door page posts to `designlab_html/join/submit.php`. It saves one row per sign-up in a MySQL table called `signups`, which it creates on the first sign-up.

## One-time setup

1. In the Electric Embers control panel, create a MySQL database and a user for it. Note the database name, user and password.
2. On the server, make a folder called `designlab-private` in the same place as `designlab_html` (next to it, not inside it).
3. Copy `config.example.php` into that folder as `config.php` and fill in the three database values.
4. Visit any door page and sign up with your own email. You should land on the thanks page and get a notification email.

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

phpMyAdmin in the control panel. Export the `signups` table as CSV to open it in Numbers.
