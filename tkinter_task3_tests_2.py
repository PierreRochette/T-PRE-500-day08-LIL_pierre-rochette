import tkinter as tk

# Fonction pour dessiner un bonhomme en bâton
def draw_stickman(canvas):
    # Dessiner les axes des abscisses et des ordonnées
    canvas.create_line(10, 250, 190, 250, fill="black", width=2)  # Axe des abscisses (X)
    canvas.create_line(100, 10, 100, 290, fill="black", width=2)  # Axe des ordonnées (Y)

    # Dessiner le corps (5 lignes)
    canvas.create_line(100, 100, 100, 200, fill="#FF0000", width=3)  # Torso (en rouge) avec une épaisseur de 3 pixels
    canvas.create_line(100, 120, 80, 160, width=2)   # Left arm avec une épaisseur de 2 pixels
    canvas.create_line(100, 120, 120, 160, width=2)  # Right arm avec une épaisseur de 2 pixels
    canvas.create_line(100, 200, 80, 250, width=2)   # Left leg avec une épaisseur de 2 pixels
    canvas.create_line(100, 200, 120, 250, width=2)  # Right leg avec une épaisseur de 2 pixels

    # Dessiner la tête (1 cercle)
    canvas.create_oval(80, 70, 120, 110, fill="white")

    # Ajouter du texte près de la tête
    canvas.create_text(100, 40, text="Stickman", font=("Arial", 12))

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

