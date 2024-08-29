from tkinter import Tk
from functions.create_ import*
from window_size import window_size
from mode.modeS import set_default

def main():
    window = Tk()
    window.title('Calculator') 
    window.geometry(f'{window_size[0]}x{window_size[1]}')
    window.resizable(0,0)

    set_default(window)

    window.mainloop()

main()