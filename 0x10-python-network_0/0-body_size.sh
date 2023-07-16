#!/bin/bash
# This script gets the byte size of the HTTP response
# header for a given URL passed as argument.
curl -s "$1" | wc -c
