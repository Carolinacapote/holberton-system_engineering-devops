# Puppet code to fix a bug

exec { 'debugging':
  command  => "sudo sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => shell;
}