# Fixes the bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`
exec { 'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
