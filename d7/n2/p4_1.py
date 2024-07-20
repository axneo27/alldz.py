d = {}

def enternew():
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

def ac1():
    print(d)  

def ac2():
    try:
        v = input("Enter value: ")
        ff = list(d.values())
        for i in range(len(ff)):
            if v not in ff:
                raise ValueError
            if ff[i] == v:
                for j in range(len(list(d))):
                    if d[list(d)[j]] == v:
                        print(f"{list(d)[j]}: {v}")
    except ValueError:
        print("Not found")


def ac3():
    try: 
        k = input("Enter key: ")
        if k not in list(d):
            raise ValueError
        v = input("Enter new value: ")
        d[k] = v
    except ValueError:
        print("Key not found")

def ac4():
    try:
        k = input("Enter key: ")
        if k not in list(d):
            raise ValueError
        print(d[k])
    except ValueError:
        print("Key not found")

def ac5():
    try:
        k = input("Enter key: ")
        if k not in list(d):
            raise ValueError
        d[k] = None
    except ValueError:
        print("Key not found")

def main():
    while True:
        action = input("\nEnter operation: \nShow dictionary|1|\nFind value|2|\nReplace value|3|\nFind value by key|4|\nDelete value by key|5|\nEnter new|6|\n")
        match action:
            case 1 | "1":
                ac1()
            case 2 | "2":
                  ac2()
            case 3 | "3":
                ac3()
            case 4 | "4":
                ac4()
            case 5 | "5":
                ac5()
            case 6 | "6":
                enternew()       