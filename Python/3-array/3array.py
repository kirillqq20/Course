numbers = list(range(1,10))
for i in numbers:
    if i % 2 == 0:
        print(i)

print("Max = " + str(max(numbers)))
print("Min = " + str(min(numbers)))
print("Sum = " + str(sum(numbers)))

num = numbers[:4]
print(num)

num1 = num[:]
del num[1]
print("=============")