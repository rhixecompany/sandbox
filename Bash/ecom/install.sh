#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

if [ -f ./ecom.socket ]
then
    mv ./ecom.socket /etc/systemd/system
fi

if [ -f /etc/systemd/system/ecom.socket ]
then  
    mv ./ecom.service /etc/systemd/system ; sudo systemctl enable ecom.service ; sudo systemctl start ecom.service
    
else
    echo "Ecom utility is not present"
fi

sudo systemctl status ecom