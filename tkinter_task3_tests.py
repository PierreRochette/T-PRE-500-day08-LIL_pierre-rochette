import tkinter as tk

# Fonction pour dessiner un bonhomme en bâton
def draw_stickman(canvas):
    # Dessiner le corps (5 lignes)
    canvas.create_line(100, 100, 100, 200)  # Torso
    canvas.create_line(100, 120, 80, 160)   # Left arm
    canvas.create_line(100, 120, 120, 160)  # Right arm
    canvas.create_line(100, 200, 80, 250)   # Left leg
    canvas.create_line(100, 200, 120, 250)  # Right leg

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
