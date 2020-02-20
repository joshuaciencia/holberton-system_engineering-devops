# fix 500 server error in apache2
exec { 'fix':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php; sudo service apache2 restart',
  provider => 'shell',
}
