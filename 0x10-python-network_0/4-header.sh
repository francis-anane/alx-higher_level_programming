#!/bin/bash
# Sends a GET request to a given URL passed as argument to the script
# with a header variable, X-School-User-Id with the value 98.
curl -sH "X-School-User-Id: 98" "${1}"
