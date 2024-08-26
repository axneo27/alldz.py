from tkinter import *
from window_size import window_size
from functions.add_functs import*
import math

values = []
def create_num_frame(window:Tk):
    global num_var, num_label
    num_var = StringVar()
    num_var.set('0')

    canvas = Canvas(window, width=500, height=100)
    canvas.place(x=0, y=30) 
    canvas.create_line(10, 90, window_size[0] - 10, 90, fill='black')
    canvas.create_line(10, 10, window_size[0] - 10, 10, fill='black')

    num_label = Label(master=canvas, textvariable=num_var, font='Calibri 28')
    num_label.place(relx=0.7, rely=0.5, anchor=E)
    window.canvas = canvas
    return num_var

def action(symbol):
    if len(values) != 1:
        current_valueStr = num_var.get()
        values.append(current_valueStr)
        values.append(symbol)
        num_var.set('')
    else:
        values.append(symbol)
        num_var.set('')     

def check_multi_div():
    i=0
    while '/' in values or '*' in values:
        if '/' not in values and '*' not in values:
            break
        elif i > len(values):
            break
        elif values[i]== '*':
            result = (float(values[i-1]))*(float(values[i+1]))
            values[i-1] = str(result)
            del values[i]
            del values[i]
            i = max(0, i - 1) 
        elif values[i]== '/':
            result = (float(values[i-1]))/(float(values[i+1]))
            values[i-1] = str(result)
            del values[i]
            del values[i]
            i = max(0, i - 1) 
        i+=1

def check_power():
    i=0
    while '^' in values:
        if '^' not in values:
            break
        elif i > len(values):
            break
        elif values[i]== '^':
            result = (float(values[i-1]))**(float(values[i+1]))
            values[i-1] = str(result)
            del values[i]
            del values[i]
            i = max(0, i - 1)
        i+=1

def see_result():
    current_valueStr = num_var.get()
    if len(values) > 1:
        values.append(current_valueStr)
        
        check_power()
        check_multi_div()
        print(values)
        while len(values) > 2:  
                if len(values)==1:
                    num_var.set(values[0])
                    break
                if values[1]== '+':
                    result = (float(values[0]))+(float(values[2]))
                    values[0] = str(result)
                    del values[1]
                    del values[1]
                elif values[1]== '-':
                    result = (float(values[0]))-(float(values[2]))
                    values[0] = str(result)
                    del values[1]
                    del values[1]
        if len(values) == 1:
            num_var.set(values[0])
            if len(values[0])>17:
                num_var.set("{:e}".format(float(values[0])))

def percent():
    current_valueStr = num_var.get()
    num_var.set(str(float(current_valueStr)*0.01))

def C():
    global M1, M2
    num_var.set('0')
    values.clear()
    M1 = 0 
    M2 = 0

def CE():
    num_var.set('0')
    po = False

def o_overX():
    current_valueStr = num_var.get()
    try:
        num_var.set(str(1/float(current_valueStr)))
    except ZeroDivisionError:
        num_var.set("ERROR")

def square():
    current_valueStr = num_var.get()
    num_var.set(str(float(current_valueStr)**2))

def sqrt():
    current_valueStr = num_var.get()
    num_var.set(str(float(current_valueStr)**0.5))

def add_to_number(newn):
    current_value = num_var.get()
    if current_value == '0' and newn!='.':
        num_var.set(newn)
    elif newn=='.' and '.' not in [i for i in current_value]:
        num_var.set(current_value+newn)
    elif len(current_value)<15 and newn!='.':
        num_var.set(current_value + newn)

def change_symbol():
    current_value = num_var.get()
    if current_value == '0':
        pass
    elif float(current_value) > 0:
        num_var.set('-'+current_value)
        for i in range(len(values)):
            if values[i]==current_value:
                values[i] = '-'+values[i]
    else:
        num_var.set(current_value.replace('-', ''))
        for i in range(len(values)):
            if values[i]==current_value:
                values[i].replace('-', '')

def erase_one():
    current_value = num_var.get()
    if len(current_value) == 1:
        num_var.set('0')
    else:
        num_var.set(current_value[:-1])

def pi():
    num_var.set(round(math.pi, 13))

def ee():
    num_var.set(round(math.e, 13))

M1 = 0
def m1():
    global M1
    if M1==0:
        M1 += float(num_var.get())
    else:
        num_var.set(str(M1))

M2 = 0
def m2():
    global M2
    if M2==0:
        M2 += float(num_var.get())
    else:
        num_var.set(str(M2))

def factor():
    n = num_var.get()
    if float(n)==int(float(n)):
        nf = math.factorial(int(float(n)))
        num_var.set(nf)
    else:
        pass