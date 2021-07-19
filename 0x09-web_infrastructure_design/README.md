# 0x09. Web infrastructure design

## Description

Learning about web infrastructure.

### Files description

- **holberton-system_engineering-devops:**  
One server web infrastructure that hosts the website that is reachable via www.foobar.com.
  - 1 server
  - 1 web server (Nginx)
  - 1 application server
  - 1 application files (your code base)
  - 1 database (MySQL)
  - 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

- **1-distributed_web_infrastructure:**  
 A three server web infrastructure that hosts the website www.foobar.com.
  We added:
  2 servers
  - 1 web server (Nginx)
  - 1 application server
  - 1 load-balancer (HAproxy)
  - 1 set of application files (your code base)
  - 1 database (MySQL)

- **2-secured_and_monitored_web_infrastructure:**  
A three server web infrastructure that hosts the website www.foobar.com, it is secured, serve encrypted traffic, and be monitored.
  We added:
  - 3 firewalls
  - 1 SSL certificate to serve www.foobar.com over HTTPS
  - 3 monitoring clients (data collector for Sumologic or other monitoring services)

## Author

| Name | GitHub username |
| ------ | ------ |
| Carolina Capote | [Carolinacapote](https://github.com/Carolinacapote) |
