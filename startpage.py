
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\HOC TAP\KLTN\GUI\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("542x375")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 375,
    width = 542,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    275.0,
    186.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    80.0,
    306.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=291.0,
    y=183.0,
    width=140.428466796875,
    height=53.970947265625
)

button_login = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_login,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_login clicked"),
    relief="flat"
)
button_2.place(
    x=104.0,
    y=184.0,
    width=140.428466796875,
    height=53.970947265625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=291.0,
    y=81.0,
    width=140.428466796875,
    height=53.970947265625
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=104.0,
    y=81.0,
    width=140.428466796875,
    height=53.970947265625
)
import os
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=229.0,
    y=267.0,
    width=73.6923828125,
    height=32.0
)
buttons_hidden=True
def show_buttons():
        if buttons_hidden:
            button_1.place(x=291.0, y=183.0, width=140.428466796875, height=53.970947265625)
            button_2.place(x=104.0, y=184.0, width=140.428466796875, height=53.970947265625)
            button_3.place(x=291.0, y=81.0, width=140.428466796875, height=53.970947265625)
            button_5.place(x=229.0, y=267.0, width=73.6923828125, height=32.0)
            

        # Update the state of button_4
        data_path = './data1/user'
        subfolders = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
        if subfolders:
            button_4.configure(state="normal")
        else:
            button_4.configure(state="disabled")
    
show_buttons()
window.resizable(False, False)
window.mainloop()