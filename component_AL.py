from abc import ABC, abstractmethod
import gfx_AL as gfx

class List_component():
    _list_of_component : list["Component"] = []
    
    def add(self,object_model):
        for comp in object_model:
            class_comp, args = comp
            self._list_of_component.append( class_comp(**args))
        
    def draw(self, x_pos, y_pos) :
        for c in self._list_of_component:
            c.draw()

class Grid(List_component):  
    _instance = None   # sentinelle pour créer un singleton
    _is_init = False   # sentinelle pour éviter un double __init__
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Grid, cls).__new__(cls)
        return cls._instance

    def __init__(self,canvas=None, w_grid_cell_size=15, h_grid_cell_size=15, **kwargs):  # corriger pour éviter plusieurs init!!!!
        if not self._is_init:
            self.w_grid_cell_size = w_grid_cell_size
            self.h_grid_cell_size = h_grid_cell_size   # hauteur de référence du nouveau système de coordonnées(basé sur les trous)
            self.canvas = canvas
            self._is_init = True
        
    def set_canvas(self,canvas):
        self.canvas = canvas
        
        
workshop = Grid()

class Component(List_component):
    
    def __init__(self, origin_x : int =0, origin_y : int=0):
        super().__init__()
        self.workshop= workshop
        self.origin_x = origin_x
        self.origin_y = origin_y
        
    def wh2xy(self,w,h):
        return w * self.workshop.w_grid_cell_size, h * self.workshop.h_grid_cell_size

    
class Hole(Component):

    def draw(self, x_pos, y_pos, scale=1):
        x, y = self.wh2xy(x_pos, y_pos)
        gfx.draw_square_hole( self.workshop.canvas, x, y, scale, space = 9)
        
class Line_of_hole(Hole):
    def __init__(self, nb_hole : int, direction : int=0):
        super().__init__()
        self.nb_hole =nb_hole
        self.direction = direction
        
    def draw(self, x_pos, y_pos, scale=1):
        for i in range(self.nb_hole):
            super().draw(x_pos + i*(1-self.direction), y_pos + i*self.direction, scale)
            
class Line_of_separator(Component):
    def __init__(self, width : int):
        super().__init__()
        self.width = width
        
    def draw(self, x_pos, y_pos, scale=1):
        x, y = self.wh2xy(x_pos, y_pos)
        w,_ = self.wh2xy(self.width, self.width)
        gfx.draw_line_separator(self.workshop.canvas, x, y, x + w, y,  scale)
            
class Board(Component):
    def __init__(self, w_board=67, h_board=23):
        super().__init__()
        self.w_board, self.h_board = self.wh2xy( w_board, h_board)
        
    def draw(self,x_pos,y_pos,scale=1):
        x, y = self.wh2xy(x_pos, y_pos)
        gfx.draw_board(self.workshop.canvas, x, y,self.h_board, self.w_board, scale)

class Rail(Component):
    def __init__(self, width : int, heigth : int):
        super().__init__()
        self.width = width 
        self.heigth = heigth

    def draw(self, x_pos, y_pos, scale=1): #coordonnees en trous 
        x, y = self.wh2xy(x_pos, y_pos)
        w,h = self.wh2xy(self.width, self.heigth)
        gfx.draw_rail(self.workshop.canvas, x, y, w, h,  scale,inter_space=self.workshop.h_grid_cell_size) 