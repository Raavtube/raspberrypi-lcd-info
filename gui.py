
# This file was partially generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
from datetime import datetime
from pathlib import Path
import threading
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import tkinter as tk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



timeA = datetime.now().strftime('%H:%M:%S')

window = Tk()
# Deployment only
window.attributes('-fullscreen', True)
timeCurrent = tk.StringVar()
window.geometry("320x480")
window.configure(bg = "#BDEB8F")


canvas = Canvas(
    window,
    bg = "#BDEB8F",
    height = 480,
    width = 320,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    15.0,
    13.0,
    anchor="nw",
    text="WELCOME RAAV",
    fill="#000000",
    font=("Rubik Regular", 36 * -1)
)
print(timeA)
timeCurrent.set(timeA)
w = tk.Label(window, textvariable=timeCurrent, background="#BDEB8F", font=("Rubik Regular", 36 * -1)).pack(pady=76)


canvas.create_text(
    22.0,
    162.0,
    anchor="nw",
    text="DISK STATUS:",
    fill="#000000",
    font=("Rubik Regular", 24 * -1)
)

canvas.create_text(
    22.0,
    200.0,
    anchor="nw",
    text="EXONMEDIA",
    fill="#000000",
    font=("Rubik Regular", 24 * -1)
)

canvas.create_text(
    22.0,
    236.0,
    anchor="nw",
    text="RAAVARCH\n",
    fill="#000000",
    font=("Rubik Regular", 24 * -1)
)

canvas.create_rectangle(
    280.0,
    203.0,
    299.0,
    222.0,
    fill="#FF3B30",
    outline="")

canvas.create_rectangle(
    280.0,
    242.0,
    299.0,
    261.0,
    fill="#FF3B30",
    outline="")

canvas.create_rectangle(
    0.0,
    62.0,
    320.0,
    71.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    135.0,
    320.0,
    144.0,
    fill="#000000",
    outline="")

def updateTime(timeX):
    canvas.create_text(
    86.0,
    80.0,
    anchor="nw",
    text=timeX,
    fill="#000000",
    font=("Rubik Regular", 36 * -1)
    )
    window.update()

window.resizable(False, False)

def exonmedia(green):
    if green == True:
        canvas.create_rectangle(
        280.0,
        203.0,
        299.0,
        222.0,
        fill="#34c759",
        outline="")
    if green == False:
        canvas.create_rectangle(
        280.0,
        203.0,
        299.0,
        222.0,
        fill="#FF3B30",
        outline="")
        
def raavarch(green):
    if green == True:
        canvas.create_rectangle(
        280.0,
        242.0,
        299.0,
        261.0,
        fill="#34c759",
        outline="")
    if green == False:
        canvas.create_rectangle(
        280.0,
        242.0,
        299.0,
        261.0,
        fill="#FF3B30",
        outline="")

def updatetime():
    while True: 
        timeA = datetime.now().strftime('%H:%M:%S')
        timeCurrent.set(timeA)
        window.update()
    
def checkDiskStatus():
    while True:
        path = "/media/pi/ENTERPRISEWORK"
        path2 = "/media/pi/RAAVARCH"
        EXONEXIST = os.path.isfile(path) 
        exonold = EXONEXIST
        RAAVEXIST = os.path.isfile(path2) 
        raavold = RAAVEXIST
        if EXONEXIST != exonold:
            exonmedia(EXONEXIST)
        if RAAVEXIST != raavold:
            raavarch(RAAVEXIST)



t_1 = threading.Thread(target=updatetime)
t_1.start()

t_2 = threading.Thread(target=checkDiskStatus)
t_2.start()




window.mainloop()

