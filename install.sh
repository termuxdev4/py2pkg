#!/bin/bash
if ! command -v wget >/dev/null 2>&1; then
  pkg install wget -y
fi
wget https://raw.githubusercontent.com/termuxdev4/py2pkg/refs/heads/main/src/py2pkg.py
mv py2pkg.py /data/data/com.termux/files/usr/bin/py2pkg
chmod +x /data/data/com.termux/files/usr/bin/py2pkg
echo "py2pkg is successfully installed!"
