import tkinter as tk
import component_AL as comp



win = tk.Tk()
win.title("Laboratoire virtuel de circuit logique - GIF-1002")
win.geometry("1500x800")  # Initial window size
#win.minsize(3456, 2234)    # Set minimal window size 3456 × 2234) 1500,800
win.resizable(True, True)  # Disabling window resizing
win.configure(bg="#330000")  # Setting consistent background color

canvas = tk.Canvas(win, width=1500, height=800, background="#333333")
canvas.pack()

#ws = comp.grid()
#ws.set_canvas(canvas)
comp.workshop.set_canvas(canvas)
bredboard = comp.Board()
bredboard.draw(3,3)

h = comp.Hole()
h.draw(4,4,scale=1)
h.draw(4,5,scale=1)

lhh = comp.Line_of_hole(5,direction=0)
lhh.draw(4,7)

ls = comp.Line_of_separator(50)
ls.draw(4,8)

r=comp.Rail(50,15)
r.draw(4,10)

r=comp.Rail(5,15) 
r.draw(4,13,scale=5)

win.mainloop()