#!/usr/bin/env bash
#the directory to backup
DIR="negpod_id-q1"
# Remote server details 
REMOTE_USER="ec1ebc754f75" 
REMOTE_HOST="ec1ebc754f75.a5efec7a.alu-cod.online" 
REMOTE_DIR="/summative/0524-2024m"

# Backup command using scp 
scp -r $DIR 
$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR 
if [ $? -eq 0 ]; then 
	echo "Backup successful." 
else echo "Backup failed." 
fi
