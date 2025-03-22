from abc import ABC, abstractmethod
import gfx_AL as gfx

#class List_component():

class Component():
    def __init__(self, origin_x : int =0, origin_y : int=0, **kwargs):
        self._list_of_component : list["Component"] = []
        self.origin_x : int = origin_x
        self.origin_y : int = origin_y
        self.item_id  : int = -1
        if type(self) != Grid:
            self.workshop = Grid()
        
    def add(self,object_model : list[tuple["Component", dict]]):
        pos = len(self._list_of_component)
        for comp in object_model:
            class_comp, args = comp
            c_temp  : Component = class_comp(**args)
            c_temp.origin_x += self.origin_x
            c_temp.origin_y +=  self.origin_y  # permet de définir la position absolue, l'utilisateur utilisant des positions relatives
            self._list_of_component.append( c_temp)
            
        return self._list_of_component[pos:]
        
    def draw(self, scale=1, **kwargs) :
        x_pos = kwargs.get("x_pos", self.origin_x)     
        y_pos = kwargs.get("y_pos", self.origin_y)   
        self.origin_x = x_pos
        self.origin_y = y_pos 
        for c in self._list_of_component:
            c.draw()
        
    def wh2xy(self,w,h):
        return w * self.workshop.w_grid_cell_size, h * self.workshop.h_grid_cell_size

class Grid(Component):  
    _instance = None   # sentinelle pour créer un singleton
    _is_init = False   # sentinelle pour éviter un double __init__
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Grid, cls).__new__(cls)
        return cls._instance

    def __init__(self,canvas=None, w_grid_cell_size=15, h_grid_cell_size=15, **kwargs):  # corriger pour éviter plusieurs init!!!!
        if not self._is_init:
            super().__init__(**kwargs)
            # self._list_of_component : list["Component"] = []
            # self.origin_x : int
            # self.origin_y : int
            # self.item_id  : int            
            self.w_grid_cell_size = w_grid_cell_size
            self.h_grid_cell_size = h_grid_cell_size   # hauteur de référence du nouveau système de coordonnées(basé sur les trous)
            self.canvas = canvas
            self._is_init = True
        
    def set_canvas(self,canvas):
        self.canvas = canvas
        
        
workshop = Grid()

class Hole(Component):

    def draw(self,scale=1, **kwargs):
        #x_pos = kwargs.get("x_pos", self.origin_x)     
        #y_pos = kwargs.get("y_pos", self.origin_y)   
        #self.origin_x = x_pos
        #self.origin_y = y_pos 
        super().draw(scale, **kwargs)
        x, y = self.wh2xy(self.origin_x, self.origin_y)
        gfx.draw_square_hole( self.workshop.canvas, x, y, scale, space = 9)
        
        
class Line_of_hole(Hole):
    def __init__(self, nb_hole : int=5, direction : int=1, **kwargs):
        super().__init__(**kwargs)
        self.nb_hole =nb_hole
        self.direction = direction
        
    def draw(self, scale=1, **kwargs):
        x_pos = kwargs.get("x_pos", self.origin_x)     
        y_pos = kwargs.get("y_pos", self.origin_y)   
        self.origin_x = x_pos
        self.origin_y = y_pos 
        for i in range(self.nb_hole):
            super().draw(scale, x_pos = x_pos + i*(1-self.direction), y_pos = y_pos + i*self.direction, **kwargs)
            
class Line_of_separator(Component):
    def __init__(self, width : int):
        super().__init__()
        self.width = width
        
    def draw(self, scale=1, **kwargs):
        x_pos = kwargs.get("x_pos", self.origin_x)     
        y_pos = kwargs.get("y_pos", self.origin_y)   
        self.origin_x = x_pos
        self.origin_y = y_pos 
        x, y = self.wh2xy(x_pos, y_pos)
        w,_ = self.wh2xy(self.width, self.width)
        gfx.draw_line_separator(self.workshop.canvas, x, y, x + w, y,  scale)
        super().draw(scale=scale, x_pos= x_pos, y_pos=y_pos, **kwargs)
        gfx.pygame.display.flip()
            
class Board(Component):
    def __init__(self, w_board=67, h_board=23, **kwargs):
        super().__init__(**kwargs)
        self.w_board, self.h_board = self.wh2xy( w_board, h_board)
        
    def draw(self, scale=1, **kwargs):
        x_pos = kwargs.get("x_pos", self.origin_x)     
        y_pos = kwargs.get("y_pos", self.origin_y)   
        self.origin_x = x_pos
        self.origin_y = y_pos 
        x, y = self.wh2xy(x_pos, y_pos)
        gfx.draw_board(self.workshop.canvas, x, y,self.h_board, self.w_board, scale)
        super().draw(scale=scale, x_pos= x_pos, y_pos=y_pos, **kwargs)
        gfx.pygame.display.flip()

class Rail(Component):
    def __init__(self, width : int, heigth : int):
        super().__init__()
        self.width = width 
        self.heigth = heigth

    def draw(self, scale=1, **kwargs): #coordonnees en trous 
        x_pos = kwargs.get("x_pos", self.origin_x)     
        y_pos = kwargs.get("y_pos", self.origin_y)  
        self.origin_x = x_pos
        self.origin_y = y_pos 
        x, y = self.wh2xy(x_pos, y_pos)
        w,h = self.wh2xy(self.width, self.heigth)
        gfx.draw_rail(self.workshop.canvas, x, y, w, h,  scale,inter_space=self.workshop.h_grid_cell_size) 