#!/bin/bash
# Send a POST request and display the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
