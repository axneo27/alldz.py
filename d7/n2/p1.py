try:
    a = float(input("Enter the number: "))
    print(a**0.5)
except ValueError:
    print("Can`t take sqrt from negative value")
except:
    print("That is not a number")