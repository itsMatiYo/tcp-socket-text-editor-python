# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# entry 3 = name field
# entry 1 = txt
# entry 2 = logs

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# ! functions
def click_join():
    """Event handler for join button"""
    print(entry_3.get())


# ! end of functions

window = Tk()

window.geometry("740x607")
window.configure(bg="#1F1F1F")

canvas = Canvas(
    window,
    bg="#1F1F1F",
    height=607,
    width=740,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(209.0, 337.0, image=entry_image_1)
entry_1 = Text(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Calibri 24"),
)
entry_1.place(x=28.0, y=95.0, width=362.0, height=482.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(569.0, 337.0, image=entry_image_2)
entry_2 = Text(bd=0, bg="#C4C4C4", highlightthickness=0)
entry_2.place(x=429.0, y=95.0, width=280.0, height=482.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(269.5, 41.0, image=entry_image_3)
entry_3 = Entry(
    bd=0,
    bg="#E7E7E7",
    highlightthickness=0,
    font=("Calibri 24"),
)
entry_3.place(x=159.0, y=15.0, width=221.0, height=50.0)

canvas.create_text(28.0,
                   24.0,
                   anchor="nw",
                   text="Name:\n",
                   fill="#FFFFFF",
                   font=("Roboto", 24 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,
                  borderwidth=0,
                  highlightthickness=0,
                  command=click_join,
                  relief="flat")
button_1.place(x=487.0, y=15.0, width=180.890625, height=51.8360595703125)
window.resizable(False, False)
window.mainloop()