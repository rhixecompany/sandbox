#!/bin/bash

sudo install -d -m 0755 /etc/apt/keyrings
sudo apt-get install wget
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc >/dev/null
gpg --with-fingerprint /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); print "\n"$0"\n"}'
Key fingerprint = 35BA A0B3 3E9E B396 F59C A838 C0BA 5CE6 DC63 15A3
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list >/dev/null
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla
sudo apt-get update && sudo apt-get install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz && tar -xvzf geckodriver-v0.35.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver
