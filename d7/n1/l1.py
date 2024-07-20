
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: ")) 
    print(a/b)
except ZeroDivisionError:
    print("Can`t divide by zero")
