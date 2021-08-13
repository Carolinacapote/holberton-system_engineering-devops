# 0x0A. Configuration management

## Description
This repository contains some tasks about configuration management with **puppet**.

### Files description

- **0-create_a_file.pp:**  
Using Puppet, create a file in `/tmp`.

- **1-install_a_package.pp:**  
Using Puppet, install `puppet-lint`.

- **2-execute_a_command.pp:**  
Using Puppet, create a manifest that kills a process named `killmenow`.

## Usage

1. Install `puppet-lint`.

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

2. Run the files

```
root@d391259bf577:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
Notice: Finished catalog run in 2.83 seconds
root@d391259bf577:/# gem list

*** LOCAL GEMS ***

puppet-lint (2.1.1)
root@d391259bf577:/#
```

## Author

| Name | GitHub username |
| ------ | ------ |
| Carolina Capote | [Carolinacapote](https://github.com/Carolinacapote) |