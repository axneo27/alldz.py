import random

l1 = []
for i in range(10):
    a = random.randrange(-100, 100)
    l1.append(a)

mx = max(l1)
mn = min(l1)

minus, plus, nul = 0, 0, 0
for i in l1:
    if i > 0:
        plus+=1
    if i < 0:
        minus+=1
    if i ==0:
        nul+=1

print(f'Maximum: {mx}\nMinimum: {mn}\nNumber of i < 0: {minus}\nNumber of i > 0: {plus}\nNumber of i = 0: {nul}\n')