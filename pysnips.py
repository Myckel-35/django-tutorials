#!/bin/env python3

# PING
import os
ping = lambda host: 0 == os.system('ping -c 1 ' + str(host) + ' &>/dev/null')
if ping("google.de"):
    print("Google is up.")
else:
    print("Google is down.")
