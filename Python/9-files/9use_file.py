input_file = "./username.txt"
output_file = "./username_output.txt"

myfile1 = open(input_file, mode = 'r', encoding='utf-8')
myfile2 = open(output_file, mode = 'w', encoding='utf-8')


for num,line in enumerate(myfile1, 1):
    if 'Russell' in line:
        print(str(num) + ' ' + line.strip())
        myfile2.write(line)

myfile1.close()
myfile2.close()