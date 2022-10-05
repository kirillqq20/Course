def fibonachi(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonachi(x-1) + fibonachi(x-2)
print(fibonachi(10))