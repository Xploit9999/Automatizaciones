#!/usr/bin/bash

mysql_root_password=${root_pass}

cat > /etc/my.cnf <<-!
[client]
user=root
password=${mysql_root_password}
!

exec "$@"
