# Puppet code to fix a bug

exec { 'debugging':
  command  => "/usr/bin/env sed -i 's/holberton/foo/' /etc/security/limits.conf",
  provider => shell;
}
