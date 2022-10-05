def main(x):
    if x == 0:
        print('End work')
    else:
        print('number = ' + str(x))
        main(x-1)


main(12)