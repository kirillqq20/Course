#!/bin/bash
echo "Enter ISBN :"
read isbn
echo $isbn | awk '/^ISBN [0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-[0-9]/' 




#ISBN 5-02-013850-9
