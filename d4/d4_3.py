a = input("enter the text: ")

b = a.split('.')
c = a.split('!')
d = a.split('?')


num = (len(b)+len(c)+len(d))-3
print(f"Number of sentences: {num}")