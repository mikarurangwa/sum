#!/bin/bash

# Directory name
DIR="negpod_id-q1"

# Check if the directory exists, if not, create it
if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi
# Move the required files to the directory
mv main.sh $DIR/
mv students_list_1023.txt $DIR/
mv select-emails.sh $DIR/
mv student-emails.txt $DIR/

echo "Files moved to $DIR."
