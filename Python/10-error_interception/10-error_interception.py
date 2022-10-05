import sys

filename = "./ussername.txt"
while True:
    try:
        print('Block try')
        myfile = open(filename, mode ='r', encoding='utf-8')
    except Exception:
        print('Exception')
        print(sys.exc_info()[1])
        filename = input('Erorr! Please enter correct file name : ')
    else:
        print('ELSE')
        print(myfile.read())
        sys.exit()