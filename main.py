from tkinter import *

# ----- COLORS ----- #
DARK_PURP = '#373854'
PURPLE = '#493267'
LIGHT_PURP = '#9e379f'


def btn_clicked():
    """
    Function that gets input from entry when the button is clicked
    """
    input = ent.get()
    ans_lbl["text"] = (int(input) * 1.609)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20, bg=PURPLE)

ent = Entry(window, width=12, bd=2, bg=LIGHT_PURP)
ent.insert(0, "0")
ent.grid(column=1, row=0)

miles_lbl = Label(window, text=" Miles", font=("Serif", 11, "normal"), bg=PURPLE, fg="white")
miles_lbl.grid(column=2, row=0)

is_equal_lbl = Label(window, text="is equal to", font=("Serif", 11, "normal"), bg=PURPLE, fg="white")
is_equal_lbl.grid(column=0, row=1)

ans_lbl = Label(window, text="0", font=("Serif", 11, "normal"), bg=PURPLE, fg="white")
ans_lbl.grid(column=1, row=1)

km_lbl = Label(window, text="Km", font=("Serif", 11, "normal"), bg=PURPLE, fg="white")
km_lbl.grid(column=2, row=1)

btn = Button(window, text="Calculate", font=("Serif", 10, "normal"), width=6, height=1, command=btn_clicked)
btn.grid(column=1, row=2)

window.mainloop()