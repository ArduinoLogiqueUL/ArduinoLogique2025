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
board_model = [(comp.Board,{"origin_x":10,"origin_y":3})]
[bredboard] = comp.workshop.add(board_model)
#line_hole_model = [(comp.Line_of_hole,{"origin_x":1,"origin_y":1,"direction":0})]
            # bredboard.add(line_hole_model)
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
running : bool = True
while running:
    theta = 0
    axe = [0,0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit