a = input("enter something: ")

a = a.lower()
b = []
for i in a:
    if i== ' ':
        continue
    b.append(i)

if b == b[::-1]:
    print("Palindrom") 
else:
    print("Not palindrom")