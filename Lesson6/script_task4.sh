#! /bin/bash
echo`lsof -u kirill | tr -s " " | cut -d" " -f1,2,3 >pid.txt`
echo "Complete"