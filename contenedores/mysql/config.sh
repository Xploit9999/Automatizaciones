#!/usr/bin/bash

function configuracion(){

    mysqld_safe --datadir="${DATA_DIR}" &
    sleep 5
    mariadb -u root -p${MYSQL_ROOT_PASSWORD} <<-!
      ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';
      CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';
      GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
      FLUSH PRIVILEGES;
!
    mysqladmin -u root -p"${MYSQL_ROOT_PASSWORD}" shutdown

}

function inicio_temporal(){

  mariadb-install-db --user=mysql --datadir="${DATA_DIR}" >/dev/null
  mysqld_safe --datadir="${DATA_DIR}" &
  sleep 5
  mysqladmin -u root shutdown

}

function __main__(){

    MYSQL_ROOT_PASSWORD="${root_pass:-default123}"
    DATA_DIR="/var/lib/mysql"

    [[ ! -d "${DATA_DIR}/mysql" ]] && { inicio_temporal ;}
    configuracion; exec "$@"
}

set -e ;__main__ "$@"
