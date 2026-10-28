<?php
// Early-access sign-ups for every door page. All forms post here.
// Database settings live outside the public folder (see server/README.md).

declare(strict_types=1);

$configPath = getenv('DL_CONFIG') ?: dirname(__DIR__, 2) . '/designlab-private/config.php';

function back(string $to): void {
    header('Location: ' . $to, true, 303);
    exit;
}

function slug(?string $v, string $default): string {
    $v = strtolower(trim((string)$v));
    return preg_match('/^[a-z0-9-]{1,40}$/', $v) ? $v : $default;
}

function text(?string $v, int $max = 100): ?string {
    $v = trim(preg_replace('/[\x00-\x1F\x7F]/u', '', (string)$v) ?? '');
    return $v === '' ? null : (function_exists("mb_substr") ? mb_substr($v, 0, $max) : substr($v, 0, $max));
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    back('/');
}

$page    = slug($_POST['page'] ?? null, 'unknown');
$cohort  = slug($_POST['cohort'] ?? null, 'unknown');
$test    = slug($_POST['test'] ?? null, 'unknown');
$variant = slug($_POST['variant'] ?? null, 'a');
$return  = '/' . trim(preg_replace('#[^a-z0-9/-]#', '', strtolower((string)($_POST['return'] ?? ''))), '/') . '/';
$thanks  = '/join/thanks/?p=' . rawurlencode($page);

// Spam: a hidden field people never see, and a too-fast submit. Bots get the
// thanks page so they don't learn anything, but nothing is saved.
$honeypot = trim((string)($_POST['website'] ?? ''));
$started  = (int)($_POST['t'] ?? 0);
$tooFast  = $started > 0 && (time() * 1000 - $started) < 2500;
if ($honeypot !== '' || $tooFast) {
    back($thanks);
}

$email = strtolower(trim((string)($_POST['email'] ?? '')));
if (strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    back($return . '?error=email#join');
}

$refHost = null;
if (!empty($_POST['ref'])) {
    $host = parse_url((string)$_POST['ref'], PHP_URL_HOST);
    $refHost = $host ? text($host, 100) : null;
}

$row = [
    'email'    => $email,
    'page'     => $page,
    'cohort'   => $cohort,
    'test'     => $test,
    'variant'  => $variant,
    'source'   => text($_POST['utm_source'] ?? null),
    'medium'   => text($_POST['utm_medium'] ?? null),
    'campaign' => text($_POST['utm_campaign'] ?? null),
    'ref_host' => $refHost,
    'landing'  => text($return, 200),
];

if (!is_file($configPath)) {
    error_log('designlab signup: config not found at ' . $configPath);
    back($return . '?error=server#join');
}
$config = require $configPath;

try {
    $db = new PDO($config['dsn'], $config['user'] ?? null, $config['pass'] ?? null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    ]);
    $isMysql = $db->getAttribute(PDO::ATTR_DRIVER_NAME) === 'mysql';
    $id = $isMysql ? 'INT UNSIGNED AUTO_INCREMENT PRIMARY KEY' : 'INTEGER PRIMARY KEY AUTOINCREMENT';
    $db->exec("CREATE TABLE IF NOT EXISTS signups (
        id $id,
        created_at VARCHAR(20) NOT NULL,
        email VARCHAR(254) NOT NULL,
        page VARCHAR(40) NOT NULL,
        cohort VARCHAR(40) NOT NULL,
        test VARCHAR(40) NOT NULL,
        variant VARCHAR(40) NOT NULL,
        source VARCHAR(100) NULL,
        medium VARCHAR(100) NULL,
        campaign VARCHAR(100) NULL,
        ref_host VARCHAR(100) NULL,
        landing VARCHAR(200) NULL,
        status VARCHAR(20) NOT NULL DEFAULT 'new',
        notes TEXT NULL,
        UNIQUE (email, page, test)
    )");

    $exists = $db->prepare('SELECT 1 FROM signups WHERE email = ? AND page = ? AND test = ?');
    $exists->execute([$row['email'], $row['page'], $row['test']]);
    if ($exists->fetchColumn()) {
        back($thanks);
    }

    $row['created_at'] = gmdate('Y-m-d H:i:s');
    $cols = implode(', ', array_keys($row));
    $marks = implode(', ', array_fill(0, count($row), '?'));
    $db->prepare("INSERT INTO signups ($cols) VALUES ($marks)")->execute(array_values($row));
} catch (Throwable $e) {
    error_log('designlab signup: ' . $e->getMessage());
    back($return . '?error=server#join');
}

if (!empty($config['notify'])) {
    $body = "New early-access sign-up\n\n";
    foreach ($row as $k => $v) {
        $body .= str_pad($k, 10) . ': ' . ($v ?? '') . "\n";
    }
    @mail(
        $config['notify'],
        'Sign-up: ' . $row['page'] . ' (' . $row['cohort'] . ')',
        $body,
        'From: ' . ($config['from'] ?? 'noreply@designlab.fyi')
    );
}

back($thanks);
