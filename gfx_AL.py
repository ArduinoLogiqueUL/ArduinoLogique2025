import tkinter as tk
import pygame
from pygame.locals import *
import pygame.gfxdraw

canvas : pygame.Surface = None

def init_gfx(width : int = None, height :int  = None, titre : str = "Arduino Logique"):
     global canvas
     #pygame.init()
     print(f"(moules ok, modules ko) = {pygame.init()}")
     if not width or not height:
            canvas = pygame.display.set_mode()
     else:  canvas = pygame.display.set_mode((width, height))
     pygame.display.set_caption(titre)
     canvas.fill((51, 51, 51))

def draw_line_separator(canvas,x_distance, y_distance, x2, y2, scale=1, width=-1, **kwargs):
    space = kwargs.get("space", 9) * scale
    if width != -1:
        scale = width / space
        
    color = kwargs.get("color", (112, 112, 112))
    thickness =  kwargs.get("thickness", 1)
    thickness = 1 * scale
    #canvas.create_line(x_distance, y_distance,x2,y2, fill=color,width=thickness, **kwargs)
    pygame.gfxdraw.hline(canvas, x_distance,x2, y_distance, color)
      
def draw_square_hole( canvas,x_distance, y_distance, scale=1, width=-1, **kwargs):
        """
        Draw a square hole at the given coordinates.
        """
        space = kwargs.get("space", 9) * scale
        if width != -1:
            scale = width / space

        #inter_space = 15 * scale

        dark_color, light_color, hole_color = kwargs.get("colors", [(192, 192, 192), (246, 246, 246), (72, 72, 72)])
        
        points = [(x_distance,
            y_distance + space),
            (x_distance,
            y_distance),
            (x_distance + space,
            y_distance)]
        pygame.gfxdraw.filled_polygon(canvas,points,dark_color)
        #pygame.gfxdraw.aapolygon(canvas,points,dark_color)
        # canvas.create_polygon(
        #     x_distance,
        #     y_distance + space,
        #     x_distance,
        #     y_distance,
        #     x_distance + space,
        #     y_distance,
        #     fill=dark_color,
        #     outline=dark_color,
        # )
        points = [(x_distance,
            y_distance + space),
            (x_distance + space,
            y_distance + space),
            (x_distance + space,
            y_distance)]
        pygame.gfxdraw.filled_polygon(canvas,points,light_color)
        # canvas.create_polygon(
        #     x_distance,
        #     y_distance + space,
        #     x_distance + space,
        #     y_distance + space,
        #     x_distance + space,
        #     y_distance,
        #     fill=light_color,
        #     outline=light_color,
        #     tags = "",
        # )
        r = pygame.Rect(    x_distance + space // 3,
                        y_distance + space // 3,
                        space // 3,
                        space // 3
                    )
        pygame.gfxdraw.box(canvas, r, hole_color)
        # item_id = canvas.create_rectangle(
        #     x_distance + space // 3,
        #     y_distance + space // 3,
        #     x_distance + 2 * space // 3,
        #     y_distance + 2 * space // 3,
        #     fill=hole_color,
        #     outline=hole_color,
        # )


        return ((x_distance, y_distance))

def rounded_rect( canvas, x: int, y: int, width: int, height: int, radius: int,outline: int, fill: int,  thickness: int, **kwargs) -> None:
    """
    Draws a rounded rectangle on a given canvas.
    Parameters:
    x (int): The x-coordinate of the top-left corner of the rectangle.
    y (int): The y-coordinate of the top-left corner of the rectangle.
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    radius (int): The radius of the corners.
    thickness (int): The thickness of the rectangle's border.
    **kwargs: Additional keyword arguments to customize the rectangle, such as:
        - fill (str): The fill color of the rectangle.
        - tags (str): Tags to associate with the rectangle.
        - outline (str): The outline color of the rectangle.
    Returns:
    None
    """

    x2 = x + width
    y2 = y + height
    points = [
        (x + radius,
        y),
        (x2 - radius,
        y),
        (x2,
        y + radius),
        (x2,
        y2 - radius),
        (x2 - radius,
        y2),
        (x + radius,
        y2),
        (x,
        y2 - radius),
        (x,
        y + radius),
    ]
    #tag = kwargs.get("tags", "")
    #fill = kwargs.get("fill", "")
    thickness = kwargs.get("thickness", 1)
    
    # Draw four arcs for corners
    #canvas.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, style=tk.PIESLICE, **kwargs)
    pygame.gfxdraw.filled_circle(canvas,x + radius,y2 -  radius,radius,fill)
#    canvas.create_arc(x2 - 2 * radius, y, x2, y + 2 * radius, start=0, extent=90, style=tk.PIESLICE, **kwargs)
    pygame.gfxdraw.filled_circle(canvas,x2 -  radius, y2  - radius,radius,fill)
    # canvas.create_arc(
    #     x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, **kwargs
    # )
    pygame.gfxdraw.filled_circle(canvas, x2 -  radius, y + radius, radius,fill)
    # canvas.create_arc(
    #     x, y2 - 2 * radius, x + 2 * radius, y2, start=180, extent=90, style=tk.PIESLICE, **kwargs
    # )
    pygame.gfxdraw.filled_circle(canvas, x + radius, y + radius, radius, fill)
    # kwargs["outline"] = fill
    # canvas.create_polygon(points, smooth=False,fill=fill, **kwargs)
    pygame.gfxdraw.filled_polygon(canvas,points,fill)
    # canvas.create_line(x + radius, y, x, y + radius, fill=fill, width=thickness)
    # canvas.create_line(x2 - radius, y, x2, y + radius, fill=fill, width=thickness)
    # canvas.create_line(x2 - radius, y2, x2, y2 - radius, fill=fill, width=thickness)
    # canvas.create_line(x, y2 - radius, x + radius, y2, fill=fill, width=thickness)


def draw_board(canvas,x_distance, y_distance,h_board, w_board, scale=1, width=-1, **kwargs):

        if width != -1:
            scale = width / 9.0
        inter_space = 15 * scale
        thickness = 1 * scale

        #dim = BOARD_830_PTS_PARAMS.copy()
        #dim["dimLine"] = kwargs.get("dimLine", dim["dimLine"])
        #dim["dimColumn"] = kwargs.get("dimColumn", dim["dimColumn"])
        color = kwargs.get("color", (240,240,220))   #"#F5F5DC"
        #sep_alim = kwargs.get("sepAlim", dim["sepAlim"])
        #sep_distrib = kwargs.get("sepDistribution", dim["sepDistribution"])
        radius = kwargs.get("radius", 5)

        thickness = 1 * scale
        #dim_line = dim["dimLine"] * inter_space
        #dim_column = dim["dimColumn"] * inter_space
        #self.id_origins["bottomLimit"] = (dim_line + x_distance, y_distance + dim_column)
        rounded_rect(
            canvas, x_distance, y_distance, w_board, h_board, radius, outline=color, fill=color, thickness=thickness
        )
        # for sep in sep_alim:
        #     self.canvas.create_line(
        #         x_distance + inter_space * sep[0],
        #         y_distance + inter_space * sep[1],
        #         x_distance - inter_space * sep[0] + dim_line,
        #         y_distance + inter_space * sep[1],
        #         fill="#707070",
        #         width=thickness,
        #     )
    

        return (x_distance, y_distance)

def draw_rail(canvas,x_distance, y_distance, w, h, scale=1, width=-1, **kwargs):#objet
    space = kwargs.get("space", 9) * scale
    if width != -1:
        scale = width / space
    ###   
    inter_space = kwargs.get("inter_space", 15)*scale
    thickness =  kwargs.get("thickness", 1)*scale
    #thickness = 1 * scale
    x2, y2 = x_distance + w * scale, y_distance
    color = kwargs.get("color", "#F5F5DC")#couleur modifier707070 pour separateur 
    darkness_factor = 0.9
    r = int(color[1:3], 16) * (darkness_factor + 0.06)
    r = int(max(0, min(255, r)))
    g = int(color[3:5], 16) * (darkness_factor + 0.06)
    g = int(max(0, min(255, g)))
    b = int(color[5:7], 16) * (darkness_factor + 0.06)
    b = int(max(0, min(255, b)))
    c = [f"#{r:02x}{g:02x}{b:02x}"]
    r = int(color[1:3], 16) * (darkness_factor) #darkness_factor facteur de luminosite reduit 
    r = int(max(0, min(255, r)))
    g = int(color[3:5], 16) * (darkness_factor)
    g = int(max(0, min(255, g)))
    b = int(color[5:7], 16) * (darkness_factor)
    b = int(max(0, min(255, b)))
    c.append(f"#{r:02x}{g:02x}{b:02x}")  #nouvelle couleur assombrie ajoute a la liste et degrade de couleur sombre
    r *= darkness_factor
    g *= darkness_factor
    b *= darkness_factor
    r = int(max(0, min(255, r)))
    g = int(max(0, min(255, g)))
    b = int(max(0, min(255, b)))
    c.append(f"#{r:02x}{g:02x}{b:02x}")
    r *= darkness_factor
    g *= darkness_factor
    b *= darkness_factor
    r = int(max(0, min(255, r)))
    g = int(max(0, min(255, g)))
    b = int(max(0, min(255, b)))
    c.append(f"#{r:02x}{g:02x}{b:02x}")
    r *= darkness_factor
    g *= darkness_factor
    b *= darkness_factor
    r = int(max(0, min(255, r)))
    g = int(max(0, min(255, g)))
    b = int(max(0, min(255, b)))
    c.append(f"#{r:02x}{g:02x}{b:02x}")
#    for sep in sep_distrib:                                    #dessiner les lignes avec des teintes differentes
    canvas.create_line(
            x_distance,                 # + inter_space * sep[0],
            y_distance,                 #+ inter_space * sep[1],
            x2,                     #x_distance + dim_line - inter_space * sep[0],
            y2,                         #y_distance + dim_line - inter_space *sep[1],
            fill=c[1],
            width=thickness,
        )
    canvas.create_line(
            x_distance,             #x_distance + inter_space * sep[0],
            y_distance + thickness,             #y_distance + inter_space * sep[1] + thickness,
            x2,                         #x_distance + dim_line - inter_space * sep[0],
            y2 + thickness,                 #y_distance + inter_space * sep[1] + thickness,
            fill=c[2],
            width=thickness,
        )
    canvas.create_line(
            x_distance,
            y_distance + 2 * thickness, #y_distance + inter_space * sep[1] + 2 * thickness,
            x2,#x_distance + dim_line - inter_space * sep[0],
            y2 + 2 * thickness,#y_distance + inter_space * sep[1] + 2 * thicnesks,
            fill=c[3],
            width=thickness,
        )
    canvas.create_line(
            x_distance, #x_distance + inter_space * sep[0],
            y_distance + 3 * thickness, #y_distance + inter_space * sep[1] + 3 * thickness,
            x2, #x_distance + dim_line - inter_space * sep[0],
            y2+ 3 * thickness,#y_distance + inter_space * sep[1] + 3 * thickness,
            fill=c[4],
            width=thickness,
        )
            #     x_distance,                 # + inter_space * sep[0],
            # y_distance,                 #+ inter_space * sep[1],
            # x2,                     #x_distance + dim_line - inter_space * sep[0],
            # y2,                         #y_distance + dim_line - inter_space *sep[1],
            # fill=c[1],
            # width=thickness,

    for dy in range(4, 11):
        canvas.create_line(
                    x_distance,
                    y_distance + dy * thickness,
                    x2,
                    y2 + dy * thickness,
                    fill=c[0],
                    width=thickness,
                )
    
    canvas.create_line(
            x_distance,
            y_distance + inter_space - 1 * thickness,
            x2,
            y2 + inter_space - 1 * thickness,
            fill=c[1],
            width=thickness,
        )
    canvas.create_line(
            x_distance,
            y_distance + inter_space - 2 * thickness,
            x2,
            y2 + inter_space - 2 * thickness,
            fill=c[2],
            width=thickness,
        )
    canvas.create_line(
            x_distance,
            y_distance + inter_space - 3 * thickness,
            x2,
            y2  + inter_space - 3 * thickness,
            fill=c[3],
            width=thickness,
        )
    canvas.create_line(
            x_distance,
            y_distance + inter_space - 4 * thickness,
            x2,
            y2 + inter_space - 4 * thickness,
            fill=c[4],
            width=thickness,
        )
    return 0