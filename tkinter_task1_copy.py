import tkinter as tk
from tkinter import * 

# IMPORT DU MODULE TKINTER

root = Tk()
root.title('Label Frame with a Frame In It')

# CREATION D'UNE FENETRE PRINCIPALE

label_frame = LabelFrame(root)
label_frame.pack(padx= 10, pady=10)

# CREATION D'UNE LABEL FRAME
# AJUSTEMENT DES MARGES

frame_in = Label(label_frame,  text= "This is the frame inside the label frime")
frame_in.pack(padx = 10, pady= 10)

# CREATION D'UNE FRAME DANS LA LABEL FRAME
# AJUSTEMENT DES MARGES DE CELLE-CI

root.mainloop()

# EXECUTION DE LA BOUCLE PRINCIPALE DE TKINTER POUR AFFICHER LA FENETRE