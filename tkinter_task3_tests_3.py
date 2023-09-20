import tkinter as tk

# Fonction pour dessiner un bonhomme en bâton
def draw_stickman(canvas):
    # Dessiner les axes des abscisses et des ordonnées
    canvas.create_line(0, 150, 200, 150, fill="black", width=2)  # Axe des abscisses (X)
    canvas.create_line(100, 0, 100, 300, fill="black", width=2)  # Axe des ordonnées (Y)

    canvas.create_line(100, 100, 100, 200)  # Torso
    canvas.create_line(100, 120, 80, 160)   # Left arm
    canvas.create_line(100, 120, 120, 160)  # Right arm
    canvas.create_line(100, 200, 80, 250)   # Left leg
    canvas.create_line(100, 200, 120, 250)  # Right leg

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Stickman")

# Créer un canevas pour dessiner
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

# Dessiner le bonhomme en bâton
draw_stickman(canvas)

# Lancer la boucle principale Tkinter
root.mainloop()

