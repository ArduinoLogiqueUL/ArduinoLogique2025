import pygame
import sys

pygame.init()

# Définition des couleurs
MENU_BG    = (30, 30, 30)   # Fond du menu
TAB_DEFAULT = (50, 50, 50)   # Onglet inactif
TAB_HOVER  = (70, 70, 70)    # Onglet survolé
TAB_ACTIVE = (90, 90, 90)    # Onglet actif
TEXT_COLOR = (255, 255, 255) # Couleur du texte
SHADOW_COLOR = (0, 0, 0)     # Couleur de l'ombre portée
 
# Paramètres de la fenêtre
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
MENU_WIDTH    = 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu type Adobe Illustrator en Pygame")

font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# Classe pour gérer un onglet du menu
class Tab:
    def __init__(self, rect, text, index):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.index = index
        self.active = False
        self.hover = False

    def draw(self, surface, font):
        # Effet d'ombre portée
        shadow_offset = 3
        shadow_rect = self.rect.copy()
        shadow_rect.x += shadow_offset
        shadow_rect.y += shadow_offset
        pygame.draw.rect(surface, SHADOW_COLOR, shadow_rect)

        # Choix de la couleur en fonction de l'état
        if self.active:
            color = TAB_ACTIVE
        elif self.hover:
            color = TAB_HOVER
        else:
            color = TAB_DEFAULT

        # Dessin de l'onglet
        pygame.draw.rect(surface, color, self.rect)
        
        # Affichage du texte centré
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update_hover(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

# Création d'une liste d'onglets
tabs = []
tab_height = 50
noms_onglets = ["Outils", "Calques", "Historique", "Couleurs", "Options"]

for i, texte in enumerate(noms_onglets):
    tab_rect = (0, i * tab_height, MENU_WIDTH, tab_height)
    tabs.append(Tab(tab_rect, texte, i))

# L'onglet par défaut actif (ici le premier onglet)
active_tab_index = 0
tabs[active_tab_index].active = True

# Boucle principale
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Détection du clic sur un onglet
            for tab in tabs:
                if tab.rect.collidepoint(event.pos):
                    # Réinitialisation de l'état actif pour tous les onglets
                    for t in tabs:
                        t.active = False
                    tab.active = True

    # Mise à jour de l'état "hover" pour chaque onglet
    for tab in tabs:
        tab.update_hover(mouse_pos)

    # Affichage du fond général et du menu latéral
    screen.fill((200, 200, 200))  # Couleur du fond principal
    pygame.draw.rect(screen, MENU_BG, (0, 0, MENU_WIDTH, SCREEN_HEIGHT))  # Fond du menu à gauche

    # Affichage des onglets
    for tab in tabs:
        tab.draw(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
