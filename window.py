from tkinter import *
from tkinter import filedialog,messagebox
import time
from filesorter import sort
import os

def btn_clicked():
    window.directory = filedialog.askdirectory()
    sort(window.directory)
    time.sleep(0.2)
    messagebox.showinfo("Done!","Files successfully sorted!")
window = Tk()
window.title("FileR pro")

window.geometry("824x500")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 824,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    424.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Label(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b0.place(
    x = 212, y = 305,
    width = 518,
    height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Label(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b1.place(
    x = 329, y = 16,
    width = 284,
    height = 40)

img2 = PhotoImage(file = f"img2.png")
b2 = Label(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b2.place(
    x = 582, y = 433,
    width = 49,
    height = 53)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0, 
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 361, y = 390,
    width = 220,
    height = 34)

img4 = PhotoImage(file = f"img4.png")
b4 = Label(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b4.place(
    x = 371, y = 104,
    width = 200,
    height = 153)

img5 = PhotoImage(file = f"img5.png")
b5 = Label(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b5.place(
    x = 0, y = 0,
    width = 206,
    height = 500)

window.resizable(False, False)
window.mainloop()
