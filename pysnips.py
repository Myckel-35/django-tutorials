#!/bin/env python3


# PING
import os
ping = lambda host: 0 == os.system('ping -c 1 ' + str(host) + ' &>/dev/null')
if ping("google.de"):
    print("Google is up.")
else:
    print("Google is down.")


# PING 2
import subprocess
def ping2(host, complete=False):
    result = subprocess.run(['ping', '-c 1', str(host)],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if(complete):
        return (result.returncode == 0, result.stdout.decode('utf-8'), result.stderr.decode('utf-8'))
    else:
        return result.returncode == 0


if ping2("google.de"):
    print("Google is up.")
else:
    print("Google is down.")
