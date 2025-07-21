#!/bin/bash

function crear_usuario(){

  if ! id ${FTP_USER} &>/dev/null; then
    useradd ${FTP_USER}; echo "${FTP_USER}:${FTP_PASS}" | chpasswd
  fi
}

function __main__(){

  crear_usuario; exec "$@"
}

set -e; __main__ "$@"
