#!/bin/bash
# Sends a request to a given URL and display only the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
