#!/bin/bash
dir="/var/log/*"
for file in `sudo ls -lS $dir`
do
if [ -f $file ]
then 
echo $file
fi 
done > var_log.txt
echo "Complete"
