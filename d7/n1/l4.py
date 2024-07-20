def sss1(s):
    try:
        s = int(s)
        return s
    except:
       print("Can`t turn this into integer")

print(sss1("123"))

def sss2(s):
    s = int(s)
    return s

try:
    sss2("asd")
except:
    print("Can`t turn this into integer")