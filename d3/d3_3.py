a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


for i in range(a, b+1):
    if i%3==0:
        f = "Fizz"
        if i%5==0:
            v = "Buzz"
            f+=v
        print(f)
        continue
    if i%5==0:
        print("Buzz ")
        continue
    print(i)