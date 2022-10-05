def roman2int(s):
    roman_dict = {'I':1,'V':5,'X':10,
    'L':50,'C':100,'D':500,'M':1000}
    roman = []
    arabic = 0
    for i in s:
        roman += i
        if len(roman) == 1:
            arabic += roman_dict[i]
        elif roman[-2] == 'I' and i == 'V':
            arabic += 3
        elif roman[-2] == 'I' and i == 'X':
            arabic += 8
        elif roman[-2] == 'X' and i == 'L':
            arabic += 30
        elif roman[-2] == 'X' and i == 'C':
            arabic += 80
        elif roman[-2] == 'C' and i == 'D':
            arabic += 300
        elif roman[-2] == 'C' and i == 'M':
            arabic += 800
        else:
            arabic += roman_dict[i]
    return arabic

def int2roman(n):
    roman_9 = ['I','II','III','IV','V','VI','VII','VIII','IX']
    roman_90 = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    roman_900 = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    roman_3000 = ['M','MM','MMM']
    roman = ''
    if 0 < n//1000 < 4:
        roman += roman_3000[(n//1000)-1]
    if n//100 > 0:
        roman += roman_900[(n//100%10)-1]
    if n//10 > 0:
        roman += roman_90[(n//10%10)-1]
    if n > 0:
        roman += roman_9[(n%10)-1]
    return roman

def pascal():
    pas1, pas2 = [1], []
    while True:
        yield (pas1)
        pas1.insert(0, 0)
        pas1.append(0)
        for i in range(len(pas1) - 1):
            pas2.append(pas1[i] + pas1[i + 1])
        pas1, pas2 = pas2, []

#def retry(fn, *args, **kwargs, max_attempts=3):
#  pass