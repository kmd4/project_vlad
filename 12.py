a = '3' * 2022
while '5555' in a or '3333' in a:
    a = a.replace('5555', '33')
    a = a.replace('3333', '55')
    print(a)
print(a)