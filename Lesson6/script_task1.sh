#! /bin/bash
for file in /usr/sbin/*
do
if [ -x $file ] 
then
echo $file
fi
done > usr_executebles.txt
echo "Complete"
