#1
def divide1(a,b):
    return a/b

try:
    print(divide1(12,0))
except ZeroDivisionError:
    print("Can`t divide by zero")

#2
def divide1(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can`t divide by zero")
        return 0

print(divide1(12,0))