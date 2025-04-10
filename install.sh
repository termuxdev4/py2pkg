#!/data/data/com.termux/files/usr/bin/bash

if ! command -v wget > /dev/null 2>&1; then
  pkg install wget -y
fi

cd ~

wget -O py2pkg.py https://raw.githubusercontent.com/termuxdev4/py2pkg/refs/heads/main/src/py2pkg.py

if ! grep -q "alias py2pkg=" ~/.bashrc; then
  echo "alias py2pkg='python3 py2pkg.py'" >> ~/.bashrc
fi

echo "py2pkg is successfully installed! At version 2.0.0"
