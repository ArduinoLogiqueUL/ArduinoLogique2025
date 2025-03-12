import tkinter as tk
import random
from PIL import Image, ImageTk

class SmokeEffect:
    def __init__(self, canvas, x1, y1, w, h, duration):
        self.canvas = canvas
        self.x1, self.y1 = x1, y1
        self.w, self.h = w, h
        self.duration = duration
        self.particles = []
        self.running = True
        
        # Charger les images de fumée avec transparence
        self.smoke_images = [
            ImageTk.PhotoImage(Image.open(f"smoke{i}.png").resize((30, 30), Image.ANTIALIAS)) 
            for i in range(1, 4)  # 3 images différentes (smoke1.png, smoke2.png, smoke3.png)
        ]
        
        self.animate_smoke()

    def create_particle(self):
        """ Crée une particule de fumée avec une image PNG. """
        size = random.randint(20, 40)  # Taille aléatoire
        x = self.x1 + random.randint(-self.w // 4, self.w // 4)
        y = self.y1

        # Choisir une image aléatoire de fumée
        img = random.choice(self.smoke_images)

        # Afficher l'image sur le canevas
        img_id = self.canvas.create_image(x, y, image=img, anchor=tk.CENTER)

        # Stocker la particule
        self.particles.append({"id": img_id, "x": x, "y": y, "life": 100, "img": img})

    def animate_smoke(self):
        """ Anime les particules de fumée en les faisant monter et s'estomper. """
        if not self.running:
            return

        for particle in self.particles:
            particle["y"] -= random.randint(1, 3)  # Monter progressivement
            particle["x"] += random.choice([-1, 0, 1])  # Légère dispersion horizontale
            particle["life"] -= 2  # Réduire la durée de vie

            self.canvas.coords(particle["id"], particle["x"], particle["y"])

            # Changer la transparence (simulation en réduisant l'opacité perçue)
            alpha = int(255 * (particle["life"] / 100))
            if alpha < 50:  # Supprimer la particule quand elle est quasi invisible
                self.canvas.delete(particle["id"])

        # Nettoyage des particules invisibles
        self.particles = [p for p in self.particles if p["life"] > 0]

        # Ajouter de nouvelles particules
        if random.random() < 0.3:
            self.create_particle()

        # Arrêter après la durée spécifiée
        if self.duration > 0:
            self.duration -= 50
            self.canvas.after(50, self.animate_smoke)
        else:
            self.running = False

# Création de l'interface Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Lancer une fumée avec images
SmokeEffect(canvas, 250, 400, 50, 100, 5000)

root.mainloop()
