#Модуль 2
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

spar = 0
avspar = 0
for i in range(a, b+1):
    if i%2!=0:
        continue
    spar+=i
    avspar+=1
print(f"Sum of even numbers: {spar}\n and the average is {spar/avspar}")

snepar = 0
avsnepar = 0
for i in range(a, b+1):
    if i%2==0:
        continue
    snepar+=i
    avsnepar+=1
print(f"Sum of odd numbers: {snepar}\n and the average is {snepar/avsnepar}")

s9 = 0
av9 = 0
for i in range(a, b+1):
    if i%9!=0:
        continue
    s9+=i
    av9+=1
print(f"Sum of numbers %9=0: {s9}\n and the average is {s9/av9}")
