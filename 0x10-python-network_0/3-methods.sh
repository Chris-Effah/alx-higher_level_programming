#!/bin/bash
# a sript that displays all the http methods a server will accept
curl -sI -X OPTIONS "$1" | grep -iE '^Allow:' | cut -d ' ' -f 2-
