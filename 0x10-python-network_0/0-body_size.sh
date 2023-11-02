#!/bin/bash
# a script that displays the size of the body of a response in bytes
curl -sI "$1" |grep -iE '^Content-Length:' | awk '{print $2}' | tr -d '\r'
