from functions.create_ import*

def set_default(window:Tk):
    for widget in window.winfo_children():
        widget.destroy()
    create_modes(window, set_default, ultra)
    create_num_frame(window)
    create_buttons09(window)
    create_right_col_buttons(window)
    create_top_buttons(window)

def ultra(window:Tk, button_height, button_width, button_star_y):
    for widget in window.winfo_children():
        widget.destroy()
    create_modes(window, set_default, ultra)
    create_buttons09(window, button_height, button_width, button_star_y)
    create_right_col_buttons(window, button_height, button_width, button_star_y)
    create_top_buttons(window, button_height, button_width, button_star_y)
    create_num_frame(window)
    create_addButtons(window, button_height, button_width, button_star_y)