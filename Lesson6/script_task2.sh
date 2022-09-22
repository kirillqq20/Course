#! /bin/bash
echo "Колличество строк: "`wc -l ./usr_executebles.txt`
echo "Первые 10 файлов: "
echo `head -10 ./usr_executebles.txt | cut -d/ -f4 >cmd_names.txt`
echo "Complete"
