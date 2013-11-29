##SSH_connection_mail
These scripts send a mail when a new SSH connection is established.

Tested on Debian.

###sshrc
This file **must** be moved to ```/etc/ssh/sshrc```. It will be called when a new connection is established, by any valid user.

In this script, you can edit the variable
``` SERVER_NAME=yourserver.com ``` with your hostname.
You can also edit the Python script path.

###ssh_connect.py
This script will be executed by the "sshrc" file. You can move it into ```/usr/local/bin/perso/ssh_connect.py```, however, you can moved it when you want on your system. In this case, don't forget to edit the sshrc file to modify the new path.

**Don't forget to modify the SMTP and email configurations in the ssh_connect.py**

If you want to test the ssh_connect.py script, you can execute de following command: ```python ssh_connect.py userName hostName userIP```