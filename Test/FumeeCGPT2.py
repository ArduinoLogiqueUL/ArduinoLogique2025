import tkinter as tk
import random
import math

class SmokeParticle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size_x = random.randint(5, 12)  # Largeur fine pour un filet de fumée
        self.size_y = random.randint(20, 40)  # Hauteur plus grande pour un effet allongé
        self.alpha = 255  # Opacité initiale
        self.dy = random.uniform(-2, -1)  # Montée douce
        self.dx = random.uniform(-0.6, 0.6)  # Légère oscillation latérale
        self.wave_amplitude = random.uniform(1, 5)  # Amplitude des ondulations
        self.life = 100  # Durée de vie en nombre de cycles

        # Créer une particule ovale fine et allongée
        gray = 150  # Gris clair
        self.color = f"#{gray:02x}{gray:02x}{gray:02x}"
        self.id = self.canvas.create_oval(
            self.x, self.y, self.x + self.size_x, self.y + self.size_y, 
            fill=self.color, outline=""
        )

    def update(self, frame):
        """Met à jour la particule : monte, oscille et s'efface progressivement."""
        self.y += self.dy  # Monter progressivement
        self.x += self.dx + self.wave_amplitude * math.sin(frame / 10)  # Oscillation sinusoïdale
        self.size_x *= 1.01  # Expansion latérale légère
        self.size_y *= 1.02  # Expansion verticale progressive
        self.life -= 2  # Réduction de la durée de vie
        self.alpha = max(0, int(255 * (self.life / 100)))  # Opacité qui diminue

        # Modifier la couleur pour un effet de disparition
        gray = max(80, 200 - (100 - self.life))
        self.color = f"#{gray:02x}{gray:02x}{gray:02x}"
        self.canvas.itemconfig(self.id, fill=self.color)
        
        # Mettre à jour la position et la taille
        self.canvas.coords(self.id, self.x, self.y, self.x + self.size_x, self.y + self.size_y)

        # Supprimer si la particule est trop transparente
        if self.life <= 0:
            self.canvas.delete(self.id)
            return False
        return True

class SmokeEffect:
    def __init__(self, canvas, x, y, duration=5000):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.duration = duration  # Durée de l'effet en millisecondes
        self.particles = []
        self.running = True
        self.frame = 0  # Compteur d'animation
        self.animate()

    def create_particle(self):
        """Crée une nouvelle particule pour le filet de fumée."""
        if random.random() < 0.7:  # Probabilité de création d'une particule
            self.particles.append(SmokeParticle(self.canvas, self.x, self.y))

    def animate(self):
        """Anime la fumée en mettant à jour toutes les particules."""
        if not self.running:
            return

        self.frame += 1  # Incrémentation du compteur de frames

        # Ajouter une nouvelle particule
        self.create_particle()

        # Mettre à jour et filtrer les particules vivantes
        self.particles = [p for p in self.particles if p.update(self.frame)]

        # Arrêter après la durée spécifiée
        if self.duration > 0:
            self.duration -= 50
            self.canvas.after(50, self.animate)
        else:
            self.running = False

# Interface Tkinter
root = tk.Tk()
root.title("Simulation de Fumée de Cigarette")

# Création du canevas
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Lancer la fumée à une position donnée (proche du bas)
smoke = SmokeEffect(canvas, 250, 450, duration=10000)

root.mainloop()
