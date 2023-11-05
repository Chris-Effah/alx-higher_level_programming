#!/usr/bin/python3

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.getheader('X-Request-Id')

print(x_request_id)
