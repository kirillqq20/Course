def facrotial(n):
    if n == 0 :
        return 1
    else:
        return n * facrotial(n-1)

print(facrotial(9))