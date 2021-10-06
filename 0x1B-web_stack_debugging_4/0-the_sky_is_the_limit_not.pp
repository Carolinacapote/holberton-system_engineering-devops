# Puppet code to fix a bug

exec { 'debugging':
  command  => "/usr/bin/env sed -i s/15/1000/ /etc/default/nginx",
  provider => shell;
}

exec { 'restart':
  command  => "usr/bin/env service nginx restart",
  provider => shell;
}
