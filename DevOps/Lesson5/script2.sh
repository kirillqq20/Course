#!/bin/bash
for dir in /etc/*
do
if [ -d $dir ] 
then
echo "Directory : $dir"
fi
done > etc_dir.txt
echo "Complete"