d = {}

def enternew():
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

def ac1():
    print(d)  

def ac2():
        v = input("Enter value: ")
        ff = list(d.values())
        for i in range(len(ff)):
            if v not in ff:
                return False
            if ff[i] == v:
                for j in range(len(list(d))):
                    if d[list(d)[j]] == v:
                        print(f"{list(d)[j]}: {v}")
                        return True


def ac3():
        k = input("Enter key: ")
        if k not in list(d):
            return False
        v = input("Enter new value: ")
        d[k] = v
        return True

def ac4():
        k = input("Enter key: ")
        if k not in list(d):
            return False
        print(d[k])
        return True

def ac5():
        k = input("Enter key: ")
        if k not in list(d):
            return False
        d[k] = None
        return True

def main():
    while True:
        action = input("\nEnter operation: \nShow dictionary|1|\nFind value|2|\nReplace value|3|\nFind value by key|4|\nDelete value by key|5|\nEnter new|6|\n")
        match action:
            case 1 | "1":
                ac1()
            case 2 | "2":
                try:
                    ac2()
                    if ac2()==False:
                        raise ValueError
                except ValueError:
                    print("Not found")
            case 3 | "3":
                try:
                    ac3()
                    if ac3()==False:
                        raise ValueError
                except ValueError:
                    print("Not found")
            case 4 | "4":
                try:
                    ac4()
                    if ac4()==False:
                        raise ValueError
                except ValueError:
                    print("Not found")
            case 5 | "5":
                try:
                    ac5()
                    if ac5()==False:
                        raise ValueError
                except ValueError:
                    print("Not found")
            case 6 | "6":
                enternew()       