from tkinter import Tk
from tkinter import Canvas

window = Tk()
window.geometry("400x400")
window.configure(background= "white")
window.title("Realistic sphere")
window.resizable(False, False)

canvas = Canvas(width=350, height=350, background="grey")
canvas.pack(padx=10, pady=10)



# CETTE PARTIE DE CODE PERMET DE CREER UN CERCLE (SI X1 = Y2 et X2 = Y1)
# Mais le cercle ne sera pas centré sur le canva
# Les coordonnées partent des bords du canva
"""
x1 = y2 = 300
x2 = y1 = 100
print(x1, x2, y1, y2)

"""

# CETTE PARTIE DE CODE PERMET DE CRÉER UN CERCLE CENTRÉ

x_center = canvas.winfo_reqwidth() / 2
y_center = canvas.winfo_reqheight() / 2 
radius = 100
x1 = x_center - radius
y1 = y_center - radius
x2 = x_center + radius
y2 = y_center + radius

canvas.create_oval(x1, y1, x2, y2, width=3)

window.mainloop()