<?php
// Copy to designlab-private/config.php on the server (next to designlab_html,
// never inside it). Never commit real values here: the repo is public.
return [
    // SQLite: the sign-ups file is created next to this config on the first sign-up.
    'dsn'    => 'sqlite:' . __DIR__ . '/signups.db',
    'user'   => null,
    'pass'   => null,
    // MySQL instead, if you ever want it (values from your Electric Embers account page):
    // 'dsn' => 'mysql:host=DB_HOST;dbname=DB_NAME;charset=utf8mb4', 'user' => 'DB_USER', 'pass' => 'DB_PASSWORD',
    'notify' => 'hello@designlab.fyi',   // one email per sign-up; '' to turn off
    'from'   => 'noreply@designlab.fyi',
];
