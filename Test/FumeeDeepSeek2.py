import tkinter as tk
import random

def fumee(x1, y1, w, h, temps):
    root = tk.Tk()
    root.title("Animation de fumée")
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Fonction pour animer la fumée
    def animer_fumee(ligne, dx, dy, alpha):
        coords = canvas.coords(ligne)
        if alpha <= 0 or coords[1] < y1 - h:  # Si la fumée sort de la zone ou devient invisible
            canvas.delete(ligne)
            return
        canvas.move(ligne, dx, dy)
        # Simuler la transparence en utilisant des couleurs de plus en plus claires
        gray_value = int(90 + (alpha / 100) * 165)  # Passer de gris foncé à clair
        canvas.itemconfig(ligne, fill=f'#{gray_value:02x}{gray_value:02x}{gray_value:02x}')
        root.after(50, animer_fumee, ligne, dx, dy, alpha - 2)  # Réduire la transparence progressivement

    # Créer plusieurs lignes fines pour simuler la fumée
    for _ in range(20):  # Nombre de lignes pour la fumée
        # Position initiale aléatoire dans la zone définie
        x_start = x1 + random.randint(0, w)
        y_start = y1 + random.randint(0, 10)  # Commence légèrement au-dessus de y1
        x_end = x_start + random.uniform(-5, 5)  # Légère variation horizontale
        y_end = y_start - random.randint(5, 15)  # Légère variation verticale (vers le haut)
        ligne = canvas.create_line(
            x_start, y_start, x_end, y_end,
            fill='#5a5a5a', width=1  # Couleur grise initiale
        )
        dx = random.uniform(-0.5, 0.5)  # Déplacement horizontal aléatoire
        dy = random.uniform(-1, -0.5)  # Déplacement vertical (vers le haut)
        alpha = 100  # Transparence initiale (simulée)
        root.after(random.randint(0, temps), animer_fumee, ligne, dx, dy, alpha)

    root.mainloop()

# Exemple d'utilisation
fumee(100, 200, 10, 50, 1000)  # x1, y1, w, h, temps en ms