import tkinter as tk
import component_AL as comp
import Devices as dev
import pygame
from pygame.locals import *
import gfx_AL as gfx



gfx.init_gfx()
# win = tk.Tk()
# win.title("Laboratoire virtuel de circuit logique - GIF-1002")
# win.geometry("1500x800")  # Initial window size
# #win.minsize(3456, 2234)    # Set minimal window size 3456 × 2234) 1500,800
# win.resizable(True, True)  # Disabling window resizing
# win.configure(bg="#330000")  # Setting consistent background color

# canvas = tk.Canvas(win, width=1500, height=800, background="#333333")
# canvas.pack()
# cursor = dev.Mouse_cursor(win = win, canvas=canvas,file_name="Images/zoom-in.png")
#ws = comp.grid()
#ws.set_canvas(canvas)
comp.workshop.set_canvas(gfx.canvas)
board_model = [(comp.Board,{"origin_x":20,"origin_y":2})]
[bredboard] = comp.workshop.add(board_model)
line_hole_model = [(comp.Line_of_hole,{"origin_x":1,"origin_y":1,"direction":0})]
bredboard.add(line_hole_model)
comp.workshop.draw()
# bredboard = comp.Board()
# bredboard.draw(x_pos = 3, y_pos =3)

# h = comp.Hole()
# h.draw(x_pos =4,y_pos =4,scale=1)
# h.draw(x_pos =4,y_pos =5,scale=1)

# lhh = comp.Line_of_hole(5,direction=0)
# lhh.draw(x_pos =4,y_pos =7)

# ls = comp.Line_of_separator(50)
# ls.draw(x_pos =4,y_pos =8)

# r=comp.Rail(50,15)
# r.draw(x_pos =4,y_pos =10)

# r=comp.Rail(5,15) 
# r.draw(x_pos =4,y_pos =13,scale=5)

#win.mainloop()
gfx.draw_menu()
# cursor_img = pygame.image.load("Images/icons/pointer2.png").convert_alpha()  
cursor_img = pygame.image.load("Images/Cur_le-curseur_blanc.png").convert_alpha()  
largeur, hauteur = cursor_img.get_size()
destination_size = (32, 32)
cursor_scaled = pygame.transform.scale(cursor_img, destination_size)

cursor_menu = pygame.image.load("Images/Cursor_menu_shadow.png").convert_alpha()  
cell_size_menu = (24, 24)
cursor_menu = pygame.transform.scale(cursor_menu, cell_size_menu)
gfx.canvas.blit(cursor_menu, (12,16))

cursor_menu = pygame.image.load("Images/Cursor_menu_blue2.png").convert_alpha()  
cell_size_menu = (24, 24)
cursor_menu = pygame.transform.scale(cursor_menu, cell_size_menu)
gfx.canvas.blit(cursor_menu, (8,12))

save_menu = pygame.image.load("Images/icons/arrow_save_menu_shadow24.png").convert_alpha()  
cell_size_menu = (24, 24)
save_menu = pygame.transform.scale(save_menu, cell_size_menu)
gfx.canvas.blit(save_menu, (12,61))

save_menu = pygame.image.load("Images/icons/arrow_save_menu_blue24.png").convert_alpha()  
cell_size_menu = (24, 24)
save_menu = pygame.transform.scale(save_menu, cell_size_menu)
gfx.canvas.blit(save_menu, (8,57))

flag_menu = pygame.image.load("Images/icons/flag_menu_yellow.png").convert_alpha()  
cell_size_menu = (24, 24)
flag_menu = pygame.transform.scale(flag_menu, cell_size_menu)
gfx.canvas.blit(flag_menu, (8,147))

chip_menu = pygame.image.load("Images/icons/chip_menu_yellow.png").convert_alpha()  
cell_size_menu = (24, 24)
chip_menu = pygame.transform.scale(chip_menu, cell_size_menu)
gfx.canvas.blit(chip_menu, (8,192))

pygame.mouse.set_visible(False)
pos = pygame.mouse.get_pos()
zone_rect = pygame.Rect(pos[0], pos[1], destination_size[0], destination_size[1])
sous_surface = gfx.canvas.subsurface(zone_rect)
copie_zone = sous_surface.copy()  
old_pos = pos
in_focus = True
running : bool = True
while running:
    theta = 0
    axe = [0,0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.WINDOWLEAVE:
           # if event.event == pygame.WINDOWEVENT_LEAVE:
            gfx.canvas.blit(copie_zone, (old_pos[0], old_pos[1]))
            in_focus = False
            # elif event.event == pygame.WINDOWEVENT_ENTER:    
            #     in_focus = 
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if in_focus:
                 gfx.canvas.blit(copie_zone, (old_pos[0], old_pos[1]))
            else: in_focus = True
            zone_rect = pygame.Rect(pos[0], pos[1], destination_size[0], destination_size[1])
            parent_rect = gfx.canvas.get_rect()
            if not parent_rect.contains(zone_rect):
                zone_rect = zone_rect.clip(parent_rect)
            sous_surface = gfx.canvas.subsurface(zone_rect)
            copie_zone = sous_surface.copy()            
            gfx.canvas.blit(cursor_scaled, pos)
            old_pos = pos

            
    pygame.display.flip()            
pygame.quit