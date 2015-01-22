#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This small script waits until the port is open a the remote computer.
    The timeout and the number of retries are defined by "max_checks" and "timeout" variables.

    This script returns 0 when the port is open, 1 if an error occurred or if the port is not available after
    all retries.

    Usage:
        wait-port-open.py {host} {port}

    Author: Charles-Emmanuel CAMUS <che.camus@gmail.com> (https://github.com/miniche/)
    License: MIT (http://opensource.org/licenses/MIT)
"""

import socket
import sys
import time

if len(sys.argv) != 3:
    print 'Usage: %s {host} {port}' % (sys.argv[0])
    exit(1)

host = sys.argv[1]
port = sys.argv[2]
max_checks = 30
timeout = 2

def check_status():
    """
    This function checks whether the asked port is open on the remote computer
    :return: 0 = the port is open, 1 = the port is closed
    """

    socket_port = socket.socket()
    socket_port.settimeout(timeout)

    try:
        socket_port.connect((host, int(port)))
        socket_port.close()
        print 'Port %s is currently open!' % (port)
        return 0
    except socket.error:
        socket_port.close()
        print 'Port %s is currently closed' % (port)
        return 1

def main():
    """
    Main logic.
    :return: 0 = running, 1 = Instance not available
    """

    print 'Checking whether the port %s is open on %s...' % (port, host)

    for i in range(0, max_checks):
        status = check_status()
        if status == 0:
            return 0

        time.sleep(5)

    print 'After %i tries, the port %s is not available. Aborting retries.' % (max_checks, port)
    return 1

exit(main())







