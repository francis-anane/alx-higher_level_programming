#!/bin/bash
# Sends a JSON POST request to a given URL passed as first argument and with a given JSON file passed as second argument.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
