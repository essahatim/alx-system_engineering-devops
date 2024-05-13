# Fix 500 error when a GET HTTP method is requested to Apache web server

exec { 'fix-issue':
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}
