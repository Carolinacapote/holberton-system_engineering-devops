# Update SSH configuration file so that you can connect to a server without typing a password.

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
        path => '/bin/'
}
