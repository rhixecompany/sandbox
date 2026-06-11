#!/bin/bash

sudo apt-get install wget unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && wget https://chromedriver.storage.googleapis.com/125.0.6422.141/chromedriver_linux64.zip

sudo dpkg -i ./google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install

unzip ./chromedriver_linux64.zip ./chromedriver && rm ./chromedriver_linux64.zip
sudo mv ./chromedriver /usr/bin/
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
