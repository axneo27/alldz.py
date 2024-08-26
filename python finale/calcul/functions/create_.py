from tkinter import *
from functools import partial
from functions.num_frame import*
from window_size import window_size

button_font = 'Calibri 16'
button_startY = 140
button_h = 60
button_w = int(window_size[0]/4)

def create_modes(window, set_default, ultra):
    standart = Button(window, text='Standart', command=partial(set_default, window))
    standart.place(y=0)
    engineering = Button(window, text='Engineering', command=partial(ultra, window, 60, window_size[0]/5, 137))
    engineering.place(y=0, x =80)

def create_buttons09(window:Tk, button_height = button_h, button_width = button_w, button_start_y = button_startY):
    buttons09 = []
    
    button0 = Button(master = window, text='0', command=partial(add_to_number, '0'), font=button_font)
    button0.place(x = button_width, y = button_height*5+button_start_y, width = button_width, height = button_height)
    buttons09.append(button0)
    xx = 0
    yy = button_height*2

    n = 7
    for i in range(0, 3):
        if i==1:
            n=8 
        elif i==2:
            n=9
        for j in range(0, 3):
            button = Button(master = window, text=f'{n}', command=partial(add_to_number, str(n)), font=button_font)
            button.place(x = xx, y = yy+button_start_y, width = button_width, height = button_height)
            if yy>button_height*3:
                yy=button_height
            yy+=button_height
            n-=3
            buttons09.append(button)
        xx+=button_width

    plusminus = Button(master = window, text=f'+/-', command=change_symbol, font=button_font)
    plusminus.place(x = 0, y = button_height*5+button_start_y, width = button_width, height = button_height)

    dot = Button(master = window, text=f'.', command=partial(add_to_number, '.'), font=button_font)
    dot.place(x = button_width*2, y = button_height*5+button_start_y, width = button_width, height = button_height)

def create_right_col_buttons(window:Tk, button_height = button_h, button_width = button_w, button_start_y = button_startY):
    buttons_rigt_col = []
    yy = 0
    for i in range(0, 6):
        button = Button(master = window, text=f'', command=None, font=button_font)
        button.place(x = button_width*3, y = yy+button_start_y, width = button_width, height = button_height)
        yy+=button_height
        buttons_rigt_col.append(button)
    
    buttons_rigt_col[0].config(command=erase_one, text='⌫')
    buttons_rigt_col[1].config(command=partial(action, '/'), text='÷')
    buttons_rigt_col[2].config(command=partial(action, '*'), text='×')
    buttons_rigt_col[3].config(command=partial(action, '-'), text='-')
    buttons_rigt_col[4].config(command=partial(action, '+'), text='+')
    buttons_rigt_col[5].config(command=partial(see_result), text='=')
    
def create_top_buttons(window:Tk, button_height = button_h, button_width = button_w, button_start_y = button_startY):
    buttonsTOP = []
    yy = 0 
    xx = 0
    for i in range(0, 2):
        for j in range(0, 3):
            button = Button(master = window, text='', command=None, font=button_font)
            button.place(x = xx, y = yy+button_start_y, width = button_width, height = button_height)
            if xx>button_width:
                xx=0
            else:
                xx+=button_width
            buttonsTOP.append(button)
        yy+=button_height

    buttonsTOP[0].config(text='%', command = percent)
    buttonsTOP[1].config(text='CE', command = CE)
    buttonsTOP[2].config(text='C', command = C)
    buttonsTOP[3].config(text='1/x', command = o_overX)
    buttonsTOP[4].config(text='x^2', command = square)
    buttonsTOP[5].config(text='sqrt(x)', command = sqrt)

def create_addButtons(window:Tk, button_height, button_width, button_start_y):
    add_butts = []
    yy = 0 
    xx = button_width*4
    for i in range(0, 6):
        button = Button(master = window, text=f'', command=None, font=button_font)
        button.place(x = xx, y = yy+button_start_y, width = button_width, height = button_height)
        yy+=button_height
        add_butts.append(button)

    add_butts[0].config(text='π', command=pi)
    add_butts[1].config(text='e', command=ee)
    add_butts[2].config(text='M1', command=m1)
    add_butts[3].config(text='M2', command=m2)
    add_butts[4].config(text='n!', command=factor)
    add_butts[5].config(text='x^', command=partial(action, '^'))

