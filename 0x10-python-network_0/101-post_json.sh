#!/bin/bash
# Send a JSON POST
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
