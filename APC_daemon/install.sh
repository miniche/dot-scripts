#!/bin/bash

# This script install "apcupsd". It is designed to minitor an APC UPS.
# You must be root to execute this.

# Author : Charles-Emmanuel CAMUS (github.com/miniche)
# License : MIT (http://opensource.org/licenses/MIT)

if [[ $EUID -ne 0 ]]; then
	echo " "
    displayError "You must be root to run the apcupsd installer!"
    exit 1
fi

echo "Updating apt repositories..."
apt-get update

echo "Getting apcupsd with apt…"
apt-get install apcupsd

echo "Done ! You can edit /etc/apcupsd/apcupsd.conf"
echo "Please read : http://doc.ubuntu-fr.org/ups_apc for more informations"
