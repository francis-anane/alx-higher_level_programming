#!/bin/bash
# This script gets the byte size of the HTTP responseheader for a given URL passed as argument.
curl -s "$1" | wc -c
