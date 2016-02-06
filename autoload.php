<?php
$phpDir = defined('PHP_DATADIR') && PHP_DATADIR ? PHP_DATADIR . '/php' : '/usr/share/php';
$pearDir = defined('PEAR_INSTALL_DIR') && PEAR_INSTALL_DIR ? PEAR_INSTALL_DIR : '/usr/share/pear';

// Use Symfony autoloader
if (!isset($loader) || !($loader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once $phpDir . '/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $loader = new \Symfony\Component\ClassLoader\ClassLoader();
    $loader->register();
}

$baseDir = __DIR__;

$loader->addPrefixes(array(
    'Symfony\\CS\\' => array($phpDir),

    // Dependencies
    'Symfony\\Component\\Console\\' => array($phpDir),
    'Symfony\\Component\\Finder' => array($phpDir),
    'Symfony\\Component\\Process\\' => array($phpDir),
    'Symfony\\Component\\EventDispatcher\\' => array($phpDir),
    'Symfony\\Component\\Stopwatch\\' => array($phpDir),
));

// Dependencies
require_once $phpDir . '/SebastianBergmann/Diff/autoload.php';

return $loader;
