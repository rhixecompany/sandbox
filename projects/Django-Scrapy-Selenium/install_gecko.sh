#!/bin/bash
sudo apt install -y snapd
sudo systemctl enable --now snapd apparmor

wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz && tar -xvzf geckodriver-v0.35.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver
sudo snap install firefox
export PATH=$PATH:/snap/bin
