import tkinter as tk


def draw_stickman(canvas) :

    #Coordonnées du bras gauche
    arm_x = 80
    arm_y = 160

    # Variable pour le mouvement du bras
    arm_direction = 1 

    def animate_arm() :
        nonlocal arm_y, arm_direction

        canvas.delete("left_arm")


        canvas.create_line(100, 100, 100, 200, width=3, fill="#0d802b") #TORSE 
        canvas.create_line(arm_x, arm_y, 80, 160, width=3, fill="#d90b0b") # left arm
        canvas.create_line(100, 120, 120, 160, width=3, fill="#230bd9") # right arm
        canvas.create_line(100, 200, 80, 250, width=3, fill="#4a024f") #left leg
        canvas.create_line(100, 200, 120, 250, width=3, fill="#bf7c08") # right leg
        canvas.create_oval(80, 70, 120, 110, width=1, fill="#15ed09") #head 
        canvas.create_text(100, 40, text="Hello World", font=("Arial", 12))

        arm_y -= arm_direction * 5

        if arm_y <= 120 or arm_y >= 160: 
            arm_direction *= -1

        canvas.after(100, animate_arm)

    animate_arm()



root = tk.Tk()
root.title("Stickman")
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

draw_stickman(canvas)
root.mainloop()