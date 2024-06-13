#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <students_file>"
    exit 1
fi

awk -F, '{print $1}' "$1"
