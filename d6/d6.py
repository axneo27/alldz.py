#EX 1
def multi(lis:list):
    m = 1
    for i in range(len(lis)):
        m*=lis[i]
    return m

#EX 2
def mini(lis:list):
    return min(lis)

#EX 3
def prost(lis:list):
    c = 0
    h = 1
    for i in range(len(lis)):
        for j in range(1, lis[i]):
            h+=1
            if lis[i]%h == 0:
                c+=1
                break
    k = len(lis) - c
    return k

#EX 4
def delete(lis:list, n):
    c = 1
    while n in lis:
        lis.remove(n)
        c +=1
    return len(lis)-c

#EX 5
def unite(lis1:list, lis2:list):
    return lis1+lis2

#EX 6
def st(lis:list, power):
    res = map((lambda x: x**power ), lis)
    return list(res)