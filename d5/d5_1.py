# EX 1
def pr():
    print('\033[90m' + "\"Don't compare yourself with anyone in this world…" 
          + '\033[35m' + "\nif" + '\033[0m' + " you" + '\033[35m' + " do so" 
          + '\33[0m' + ", you are insulting yourself." + '\033[90m' + "\"")
# pr()

# EX 2
def par(a, b):
    for i in range(a, b +1):
        if i%2 !=0:
            continue
        print(f'{i} ', end='')
# par(1, 10)

# EX 3
def square(length, sy, fill):
    p = ' '
    if fill:
        for i in range(length):
            print(sy*length)
    else:
        for i in range(length):
            if i == 0 or i == length-1:
                print(sy*length)
                continue
            print(f'{sy}{p*(length-2)}{sy}')
# square(4, '&', False)

# EX 4
def min5(n1, n2, n3, n4, n5):
    l = [n1, n2, n3, n4, n5]
    return min(l)
# min5(12, 34, 663, 88, 1)

# EX 5
def multi(st, fin):
    m = 1
    if st > fin:
        temp = fin
        fin = st
        st = temp
    for i in range(st, fin+1):
        m*=i
    return m
# multi(6, 3)

# EX 6
def co(num):
    num = str(num)
    return len(num)
# co(123678964)

# EX 7
def pali(number):
    number = str(number)
    b = []
    for i in number:
        b.append(i)
    if b == b[::-1]:
        return True
    return False
# pali(546645)