<?php
// Copy to ~/designlab-private/config.php on the server (next to designlab_html,
// never inside it) and fill in the values from the Electric Embers control panel.
// This file is never committed with real values: the repo is public.
return [
    'dsn'    => 'mysql:host=localhost;dbname=DATABASE_NAME;charset=utf8mb4',
    'user'   => 'DATABASE_USER',
    'pass'   => 'DATABASE_PASSWORD',
    'notify' => 'hello@designlab.fyi',   // gets an email per sign-up; '' to turn off
    'from'   => 'noreply@designlab.fyi',
];
