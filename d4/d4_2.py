a = input("enter the text: ")
b = input("enter reserved words: ")

if ' ' in b:    
    d = b.split()
else: 
    b= b

a = a.split()
result = []

for i in a:
    pu = ''
    for j in [',', '.', '?', '!', ':', ';']:
        if i.endswith(j):
            pu = j
            i = i[:-1] 
            break
    
    if i in d:
        i = i.upper()
    
    result.append(i + pu)

re = ' '.join(result)

print(re)