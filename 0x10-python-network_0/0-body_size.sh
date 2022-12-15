#!/bin/bash
# write a bash script that send request and display response
curl -s "$1" | wc -c
