# Debian-scripts #

This repository contains scripts that I created for some needs.

All this scripts are on MIT License (http://opensource.org/licenses/MIT)

__You can fork this repository, do some amazing changes and submit a pull request!__
__Feel free to contact me for suggestions or informations, you're always welcome.__

----

## ACP_daemon ##

Some scripts made for "apcupsd" (a daemon to manage APC UPS models : www.apc.com)
Daemon and scripts are tested with a APC Back-UPS Pro 900.

__install.sh__ = Installing the apcupsd daemon and dependancies.

To execute it :
```bash
chmod +x install.sh;
./install.sh;
```


__Others scripts__ : put them in "/etc/apcupsd" and personalize them.
They are built to send a mail for some events :
- onbattery
- offbattery
- changeme
- commok
- commfailure
- killpower


Don't forget to change emails addresses in each scripts.
Scripts will be called by apcupsd daemon when events are triggered.

----

