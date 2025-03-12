from PIL import Image, ImageTk
import tkinter as tk

class Mouse_cursor():
    file_name_cursor = ""
    file_name_swip_out = "Images/SwipOut.png"
    file_name_swip_in = "Images/SwipIn.png"
    file_name_move = "Images/Move.png"
    current_cursor_id : int = 0 
    swip_out_id : int = 0
    swip_in_id : int = 0
    mouse_x : int = 0
    mouse_y : int = 0
    #file_name_swip_out = "Images/SwipOut.png"
    def __init__(self, file_name : str = "", win : tk.Tk = None, canvas : tk.Canvas = None, **kwargs):
        self.win = win
        self.canvas = canvas
        self.file_name_cursor = file_name
        if file_name != "":
            image = Image.open(file_name)  # Chemin de votre fichier
            image = image.resize((32, 32))  # Ajuster la taille si nécessaire
            self.cursor_image = ImageTk.PhotoImage(image)
            
            self.cursor_id = self.canvas.create_image(10,10, image=self.cursor_image)  #, tags="cursor"
            self.current_cursor_id = self.cursor_id
            
            image = Image.open(self.file_name_swip_out)  # Chemin de votre fichier
            image = image.resize((32, 32))  # Ajuster la taille si nécessaire
            self.swip_out_image = ImageTk.PhotoImage(image)
            self.swip_out_id = self.canvas.create_image(-10,-10, image=self.swip_out_image)

            image = Image.open(self.file_name_swip_in)  # Chemin de votre fichier
            image = image.resize((32, 32))  # Ajuster la taille si nécessaire
            self.swip_in_image = ImageTk.PhotoImage(image)
            self.swip_in_id = self.canvas.create_image(-10,-10, image=self.swip_in_image)

            # Masquer le curseur natif
            self.win.config(cursor="none")

            # Lier le mouvement de la souris
            self.win.bind("<Motion>", self.move_cursor)
        else: self.win.config(cursor="arrow")
        
    def change_cursor(self, cursor_id : int ):
        self.canvas.itemconfig(self.current_cursor_id, state="hidden")
        self.canvas.coords(cursor_id, self.mouse_x, self.mouse_y)
        self.canvas.itemconfig(cursor_id, state="normal")
        

    def move_cursor(self, event):
        """ Déplace le curseur personnalisé en suivant la souris """
        self.mouse_x, self.mouse_y = event.x, event.y
        self.canvas.lift(self.current_cursor_id)
        self.canvas.coords(self.current_cursor_id, event.x, event.y)
