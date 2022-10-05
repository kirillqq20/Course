def myfunc (name):
    print('Congratulation ' + name )


myfunc('Ivan')

def sum (a,b) :
    s = a + b
    print(s)
sum(14,11)

def factorial (x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result
print( factorial(7))

print("========================================================================================================================")

for i in range(1,10):
    print(str(i) + '\t= ' + str(factorial(i)))

print("========================================================================================================================")

def create_record(fname,lname,email):
    record = {
        'fname': fname,
        'lname' : lname,
        'email' : email
    }
    return record

user1 = create_record('Egor', 'Zacharov','egaga@gmail.com')
user2 = create_record('Kirill', 'Krush','krush@gmail.com')

print(user1)
print("========================================================================================================================")
def add (titul,*persons):
    for person in persons :
        print ('Who : ' + person.title() + ' , titul : ' + titul )

add('Magistr','Egor')