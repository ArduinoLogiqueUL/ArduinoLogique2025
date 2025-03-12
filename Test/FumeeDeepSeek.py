import tkinter as tk
import random

def fumee(x1, y1, w, h, temps):
    root = tk.Tk()
    root.title("Animation de fumée")
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Fonction pour animer la fumée
    def animer_fumee(cercle, dx, dy, alpha):
        x0, y0, x1, y1 = canvas.coords(cercle)
        if alpha <= 0:
            canvas.delete(cercle)
            return
        canvas.move(cercle, dx, dy)
        canvas.itemconfig(cercle, fill=f'gray{int(alpha)}')
        root.after(50, animer_fumee, cercle, dx, dy, alpha - 1)

    # Créer plusieurs cercles pour simuler la fumée
    for _ in range(10):  # Nombre de cercles pour la fumée
        cercle = canvas.create_oval(
            x1, y1, x1 + random.randint(10, 30), y1 + random.randint(10, 30),
            fill='gray90', outline='gray90'
        )
        dx = random.uniform(-1, 1)  # Déplacement horizontal aléatoire
        dy = random.uniform(-2, -1)  # Déplacement vertical (vers le haut)
        alpha = 90  # Transparence initiale
        root.after(random.randint(0, temps), animer_fumee, cercle, dx, dy, alpha)

    root.mainloop()

# Exemple d'utilisation
fumee(100, 100, 30, 30, 1000)  # x1, y1, w, h, temps en ms