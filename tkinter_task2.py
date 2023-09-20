import tkinter as tk
from tkinter import * 
from tkinter import Canvas
from PIL import Image


root = Tk()
root.title('Label Frame with a Frame In It')

label_frame = LabelFrame(root)
label_frame.pack(padx= 10, pady=10)


frame_in = Label(label_frame,  text= "This is the frame inside the label frime")
frame_in.pack(padx = 10, pady= 10)

canvas = Canvas(frame_in, width=300, height=300)
canvas.pack()

image = Image.open("full-moon-friday-300x300.jpeg")
image = image.convert("RGB")
image.save("full-moon-friday-300x300.gif", "GIF")
image = PhotoImage(file='full-moon-friday-300x300.gif')
canvas.create_image(0, 0, anchor=NW, image=image)

root.mainloop()

