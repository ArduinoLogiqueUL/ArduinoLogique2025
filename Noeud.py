from enum import Enum, auto
import networkx as nx

class Type(Enum):
    VOID        = auto()
    VCC         = auto()
    GND         = auto()
    PIN_VCC     = auto()
    PIN_GND     = auto()
    PIN_INPUT   = auto()
    PIN_OUTPUT  = auto()
    PIN_CLOCK  = auto()
    FLAG_INPUT  = auto()
    (FLAG_OUTPUT) = auto()
    FLAG_CLOCK  = auto()
    HOLE        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()
    # VOID        = auto()

class Noeud:
    _id : int = 0

    def __init__(self, id = None, position = "", type_ = Type.VOID, func = "", nb_int : int = 2):
        Noeud._id += 1
        self._id_user = id
        if (id == None):
            self._id_user = self._id
        self._position : str = position
        self._type : Type = type_
        self._func : str = func
        self_nb_in : int = nb_int
        #self._func_id : int = func_id

    def __str__(self):
        return f"user id : {self._id_user} \nposition: {self._position} \ntype : {self._type} \nfunc : {self._func} \n"
    
    def __eq__(self, n):# eviter une mauvaise initialisation avec un mauvais type
        # return self.type == n.type
        return isinstance(n, Noeud) and self.type == n.type

    def __eq__(self, t:Type):
#        return self.type == t
        return isinstance(t, Type) and self.type == t

    def __hash__(self):
        return  hash(self.type)


    @property
    def id_user(self):   # Getter
        return self._id_user
    
    @id_user.setter
    def id_user(self, new_id_user):       # Setter
        self._id_user = new_id_user

    @property
    def position(self):   # Getter
        return self._position
    
    @position.setter
    def position(self, new_position):       # Setter
        self._position = new_position

    @property
    def type(self):   # Getter
        return self._type
    
    @type.setter
    def type(self, new_type):       # Setter
        self._type = new_type

    @property
    def func(self):   # Getter
        return self._func
    
    @func.setter
    def func(self, new_func):       # Setter
        self._func = new_func
    
    @property
    def func_id(self): # Getter   # Getter
        return self._func_id
    
    @func_id.setter
    def func_id(self, new_func_id): # Setter       # Setter
        self._func_id = new_func_id







    