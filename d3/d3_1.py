a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(a, b+1):
    if i%7!=0:
        continue
    print(f'{i} ', end='')