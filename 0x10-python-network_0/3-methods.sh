#!/bin/bash
# Send a request to the server and retrieve the allowed methods
curl -sI "$1" | grep -i '^Allow:' | cut -d' ' -f2-
