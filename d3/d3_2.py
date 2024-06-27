a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("All numbers in your range: ")
for i in range(a, b+1):
    print(f'{i}, ', end = '')
print("\n\nAll numbers in your range (decreasing): ")
for i in range(b, a-1, -1):
    print(f'{i}, ', end = '')
print("\n\nAll numbers in your range that are dividible by 7 without rest: ")
for i in range(a, b+1):
    if i%7!=0:
        continue
    print(i, end='')
cr5 = 0
for i in range(a, b+1):
    if i%5!=0:
        continue
    cr5+=1
print(f"\n\nNumber of numbers that are dividible by 5 without rest: {cr5}")