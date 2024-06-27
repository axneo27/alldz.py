while True:
    a = int(input("Enter the number (exit=7): "))
    
    if a > 0 and a != 7:
        print("Number is positive")
    elif a < 0:
        print("Number is negative")
    elif a == 0:
        print("Number is equal to zero")
    elif a == 7:
        print("Good bye!")
        break
