from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\HOC TAP\KLTN\GUI\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def handle_enter(event):
    print("Enter pressed, switching to frame 1")


window = Tk()
window.geometry("594x368")
window.configure(bg="#FBFBFB")

canvas = Canvas(
    window,
    bg="#FBFBFB",
    height=368,
    width=594,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    304.0,
    184.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1_state = "normal"  # Trạng thái mặc định của nút
data_path = './data1/user'
if any(Path(data_path).is_dir() for path in Path(data_path).iterdir()):
    button_1_state = "disabled"  # Nếu có folder, tắt nút

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    state=button_1_state  # Cập nhật trạng thái của nút
)
button_1.place(
    x=90.0,
    y=98.0,
    width=217.0,
    height=61.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=95.0,
    y=199.0,
    width=205.0,
    height=56.0
)
window.resizable(False, False)
window.mainloop()
