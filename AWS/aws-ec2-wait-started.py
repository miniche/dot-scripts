#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This small script waits until the EC2 instance is up.
    It uses the AWS commandline tool, available at https://aws.amazon.com/cli/.

    It must be already configured with your AWS credentials.
    Online documentation: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html

    This script returns 0 when the instance is up, 1 if an error occurred or if the instance is not available after
    all retries.

    Usage:
        wait-port-open.py {host} {port}

    Author: Charles-Emmanuel CAMUS <che.camus@gmail.com> (https://github.com/miniche/)
    License: MIT (http://opensource.org/licenses/MIT)
"""

import json
import shlex
import subprocess
import sys
import time

if len(sys.argv) == 1:
    print 'Usage: %s {instance_id}' % (sys.argv[0])
    exit(1)

instance_id = sys.argv[1]
max_checks = 30

def check_status():
    """
    This function checks whether the EC2 Instance is available, using the AWS CLI.
    :return: 0 = running, 1 = Not running yet, 2 = Stopped
    """
    command = 'aws ec2 describe-instances --instance-ids %s' % instance_id
    list_command = shlex.split(command)

    result = subprocess.Popen(list_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

    try:
        answer = json.loads(result)
    except ValueError:
        print 'AWS error. The CLI has not returned a valid JSON response!'
        print result
        return 2

    actual_status = answer['Reservations'][0]['Instances'][0]['State']['Name']
    if actual_status == 'running':
        print 'Instance running!'
        return 0
    elif actual_status == 'stopped':
        print 'Instance stopped!'
        return 2

    print 'Not running yet. Actual status: %s' % (actual_status)
    return 1

def main():
    """
    Main logic.
    :return: 0 = running, 1 = Instance not available
    """
    for i in range(0, max_checks):
        status = check_status()
        if status == 0:
            return 0
        elif status == 2:
            return 1

        time.sleep(5)

    print 'After %i tries, the EC2 instance is not available. Aborting retries.' % (max_checks)
    return 1

exit(main())







