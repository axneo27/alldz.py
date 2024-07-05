a = input("Enter the problem: ")

plus = a.split('+')
minus = a.split('-')
multi = a.split('*')
divide = a.split('/')

l1 = [plus, minus, multi, divide]

n = 0
for i in l1:
    if len(i) == 2:
        c = -1
        for j in i:
            c+=1
            i[c] = int(i[c])
        break
    n+=1

match n:
    case 0:
        print(plus[0]+plus[1])
    case 1:
        print(minus[0]-minus[1])
    case 2:
        print(multi[0]*multi[1])
    case 3:
        print(divide[0]/divide[1])
    case _:
        print("invalid")