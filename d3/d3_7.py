su = 0
maxi, mini = None, None
while True:
    a = int(input("Enter the number (exit=7): "))
    if a == 7:
        print("Good bye!")
        break
    su+=a
    if maxi == None or a > maxi:
        maxi = a
    if mini == None or a < mini:
        mini = a
    print(f'Sum: {su}\n Max: {maxi}\n Min: {mini}')