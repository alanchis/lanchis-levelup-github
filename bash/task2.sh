#!/bin/bash

#  Email alert when disk utilization is above a threshold

# Define threshold
ALERT="5"

# Define date 
NOW=$(date)

# Define Filesystem
FILESYSTEM_PATH="/dev/sda3"


#Select a specific name of your disk and pass it to the DISK_UTILIZATION variable
DISK_UTILIZATION=$( df -H |  awk '/sda3/ { print $5 }' | sed 's/%//' )
# DISK_UTILIZATION=3

echo "${DISK_UTILIZATION}" 


# If statement to evaluate if the disk utilization is greater than the threshold

if [[ $DISK_UTILIZATION -ge $ALERT ]]
then
    sendEmail

fi