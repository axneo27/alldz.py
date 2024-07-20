def sq1(n):
    return n**0.5

try:
    sq1(-1)
except ValueError:
    print("Can`t take sqrt from negative value")
except:
    print("That is not a number")

def sq2(n):
    try:
        return n**0.5
    except ValueError:
        print("Can`t take sqrt from negative value")
    except:
        print("That is not a number")

sq2(2)