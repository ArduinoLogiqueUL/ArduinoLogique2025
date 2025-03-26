from Noeud import *
import networkx as nx

circuit_test_vcc_gnd_cc = [(Type.VCC,"p3"), (Type.HOLE,"i3"), (Type.HOLE,"h3"), (Type.HOLE,"h5"), (Type.HOLE,"j5"), (Type.GND,"n5"), 
                            (Type.GND,"n9"), (Type.VCC,"p9"), (Type.GND,"n15"), (Type.HOLE,"j15"),  (Type.HOLE,"a21"), 
                            (Type.VCC,"p21"), (Type.VCC,"p27"), (Type.HOLE,"j27"), (Type.HOLE,"g27"), (Type.HOLE,"c27"), (Type.HOLE,"b27"),
                            (Type.HOLE,"b32"), (Type.HOLE,"i27"), (Type.HOLE,"i29"), (Type.HOLE,"j29"), (Type.HOLE,"j30"), 
                            (Type.VCC,"p34"), (Type.VCC,"p37"), (Type.HOLE,"c35"), (Type.HOLE,"c40"), (Type.HOLE,"d36"), (Type.HOLE,"d44"),
                            (Type.HOLE,"b40"), (Type.HOLE,"a40"), (Type.HOLE,"b44"), (Type.GND,"n40"), (Type.VCC,"p42"), (Type.HOLE,"i42"), 
                            (Type.GND,"n48"), (Type.HOLE,"j48"), (Type.HOLE,"h48"), (Type.HOLE,"h54"), (Type.HOLE,"i54"), (Type.HOLE,"i57"),
                            (Type.HOLE,"g57"), (Type.HOLE,"c57"), (Type.HOLE,"b57"), (Type.HOLE,"b51"),
                            (Type.PIN_VCC,"f15"), (Type.PIN_INPUT,"f16"),(Type.PIN_INPUT,"f17"),(Type.PIN_OUTPUT,"f18"),
                            (Type.PIN_INPUT,"f19"),(Type.PIN_INPUT,"f20"),(Type.PIN_OUTPUT,"f21"),
                            (Type.PIN_INPUT,"e15"),(Type.PIN_INPUT,"e16"),(Type.PIN_OUTPUT,"e17"),
                            (Type.PIN_INPUT,"e18"),(Type.PIN_INPUT,"e19"),(Type.PIN_OUTPUT,"e20"), (Type.PIN_GND,"e21"), 
                            (Type.PIN_VCC,"f30"), (Type.PIN_INPUT,"f31"),(Type.PIN_INPUT,"f32"),(Type.PIN_OUTPUT,"f33"),
                            (Type.PIN_INPUT,"f34"),(Type.PIN_INPUT,"f35"),(Type.PIN_OUTPUT,"f36"),
                            (Type.PIN_INPUT,"e30"),(Type.PIN_INPUT,"e31"),(Type.PIN_OUTPUT,"e32"),
                            (Type.PIN_INPUT,"e33"),(Type.PIN_INPUT,"e34"),(Type.PIN_OUTPUT,"e35"), (Type.PIN_GND,"e36"), 
                            ]
edges_vcc_gnd = [(1,2), (2,3), (3,4), (4,5), (5,6), (7,8), (9,10), (10,45), (58,11), (11,12), [13,14], (14,15), (15,16), (16,17), (17,18), (18,68),
         (14,19), (19,20), (20,21), (21,22), (22,59), (23,24), (71,25), (25,26), (72,27), (27,28), (28,31), (29,31), (29,26), (29,30), (30,32),
         (33,34), (35,36), (36,37), (37,38), (38,39), (39,40), (40,41), (41,42), (42,43), (43,44)]

circuit_test_pin_vcc_gnd_Nopwr_MB = []  #  à remplir
edges_pin_vcc_gnd_Nopwr_MB = []   #  à remplir

circuit_test_pin_in_et_pin_out = []  #  à remplir
edges_pin_in_et_pin_out= []   #  à remplir

circuit_test_flag_out_cc_mb = []  #  à remplir
edges_flag_out_cc_mb= []   #  à remplir

circuit_test_pin_clock = []  #  à remplir
edges_pin_clock = []   #  à remplir


def creation_graphe(liste_noeud : list, liste_edge : list) -> nx.Graph:
    noeuds : dict = {}
    G = nx.Graph()
    for i,n in enumerate(liste_noeud):
        t, p = n
        noeuds[str(i+1)] = Noeud( type_= t, position=p)
        print(f"{i+1} :    {noeuds[str(i+1)]}")
        G.add_node(noeuds[str(i+1)], type = noeuds[str(i+1)].type)
        
    list_edges = [(noeuds[str(e[0])], noeuds[str(e[1])]) for e in liste_edge]
    G.add_edges_from(list_edges)
        
    return G
        
def is_vcc_gnd_in_CC(g : nx.Graph):
    vcc_to_gnd : list[list[(str, Type)]]= []     
    vcc_to_pin_gnd_or_pin_out : list[list[Noeud]]= [] 
    gnd_to_pin_vcc_or_pin_out : list[list[Noeud]]= [] 
    
    # a compléter
    
    return vcc_to_gnd, vcc_to_pin_gnd_or_pin_out, gnd_to_pin_vcc_or_pin_out

def is_vcc_gnd_in_CO(g : nx.Graph):
    vcc_to_hole : list[list[(str, Type)]]= []
    gnd_to_hole : list[list[(str, Type)]]= []
    
    # à terminer
    
    return vcc_to_hole, gnd_to_hole


def is_vcc_gnd_in_no_pwr_or_MB(g : nx.Graph):
    pin_vcc_gnd_no_pwr : list[(str, Type)] = []
    pin_vcc_gnd_mb :list[list[Noeud]]= [] 
    
    # à terminer
    
    return pin_vcc_gnd_no_pwr, pin_vcc_gnd_mb

def is_pin_in_ok(g : nx.Graph):
    pin_in_cc : list[list[Noeud]]= [] 
    pin_out_cc :list[list[Noeud]]= [] 
    pin_in_mb :list[list[Noeud]]= [] 
    pin_out_mb :list[list[Noeud]]= [] 
    pin_out_co :list[list[Noeud]]= [] 
    
    # à terminer avec ce principe:
    # il y a CC si une pin_in est connecter à plus d'un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    # il y a CC si une pin_out est connecter à plus d'un de ces choix:  FLAG_OUTPUT
    # il y a CC si une pin_in est connecter à un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    # il y a mauvais branchement mb si une pin_in est connectée à : FLAG_OUTPUT ou FLAG_CLOCK
    # il y a mauvais branchement mb si une pin_out est connectée à : FLAG_INPUT ou FLAG_CLOCK
    # il y a co si une pin_out a au moins une de ses entrées non connectée, si aucune entrée n'est connectée
    # on a un état nc qui n'est pas bloquant. La propriété _nb_in contient le nombre d'entrées d'un pin_out
    # Il y a aussi co si un pin_out n'est pas connecté et qu'il y a au moins une entrée active.
    
    return pin_in_cc, pin_out_cc, pin_in_mb, pin_out_mb, pin_out_co

def is_flag_out_mb(g :nx.Graph):
    flag_out_mb :list[list[Noeud]]= [] 
    
    # a compléter
    
    return flag_out_mb

def is_pin_clock_ok(g :nx.Graph):
    pin_clock_ko :list[list[Noeud]]= [] 
    
    # a compléter
    
    return pin_clock_ko


g = creation_graphe(circuit_test_vcc_gnd_cc, edges_vcc_gnd)
vcc_to_gnd, vcc_to_pin_gnd_or_pin_out, gnd_to_pin_vcc_or_pin_out = is_vcc_gnd_in_CC(g)
print(vcc_to_gnd)
# résultat attendu : [[("p3", Type.VCC), ("i3", Type.HOLE), ("h3", Type.HOLE), ("h5", Type.HOLE), ("j5", Type.HOLE), ("n5", Type.GND)], 
# suite               [("n9", Type.GND), ("p9", Type.VCC)]]
print(vcc_to_pin_gnd_or_pin_out)
# résultat attendu : [[("n21", Type.VCC), ("a21", Type.HOLE), ("e21", Type.PIN_GND)], 
# suite               [("p27", Type.VCC), ("j27", Type.HOLE), ("g27", Type.HOLE), ("c27", Type.HOLE), ("b27", Type.HOLE), ("b32", Type.HOLE), 
# suite                ("e32", Type.PIN_OUT)]]
print(gnd_to_pin_vcc_or_pin_out)
# résultat attendu : [[("n15", Type.GND), ("j15", Type.HOLE), ("f15", Type.PIN_VCC)], 
# suite               [("n40", Type.GND), ("a40", Type.HOLE), ("c40", Type.HOLE), ("c35", Type.HOLE), ("e35", Type.PIN_OUT)]]

vcc_to_hole, gnd_to_hole = is_vcc_gnd_in_CO(g)
print(vcc_to_hole)
# résultat attendu : [[("p42", Type.VCC), ("i42", Type.HOLE)]] 
print(gnd_to_hole)
# résultat attendu : [[("n48", Type.GND), ("j48", Type.HOLE), ("h48", Type.HOLE), ("h54", Type.HOLE), ("i54", Type.HOLE), ("i57", Type.HOLE),
# suite                ("g57", Type.HOLE), ("c57", Type.HOLE), ("b57", Type.HOLE), ("b51", Type.HOLE)]] 

g = creation_graphe(circuit_test_pin_vcc_gnd_Nopwr_MB, edges_pin_vcc_gnd_Nopwr_MB)
pin_vcc_gnd_no_pwr, pin_vcc_gnd_mb = is_vcc_gnd_in_no_pwr_or_MB(g)
print(pin_vcc_gnd_no_pwr)
# résultat attendu : [("f4", Type.PIN_VCC), ("e10", Type.PIN_GND), 
#                     ("f21", Type.PIN_VCC), ("e27", Type.PIN_GND), 
#                     ("f45", Type.PIN_VCC), ("e51", Type.GND)
#                    ]

print(pin_vcc_gnd_mb) 
# résultat attendu : [[("f21", Type.PIN_VCC), ("i21", Type.FLAG_INPUT)], 
# suite               [("e27", Type.PIN_GND), ("a27", Type.FLAG_OUTPUT)],
#                     [("e38", Type.PIN_OUT), ("c38", Type.HOLE), ("c39", Type.HOLE)], ("e39", Type.PIN_GND)], 
# suite               [ ("f45", Type.PIN_VCC), ("i45", Type.FLAG_CLOCK)], [("e51", Type.PIN_GND), ("b51", Type.FLAG_CLOCK)]]

g = creation_graphe(circuit_test_pin_in_et_pin_out, edges_pin_in_et_pin_out)
pin_in_cc, pin_out_cc, pin_in_mb, pin_out_mb, pin_out_co = is_pin_in_ok(g)
print(pin_in_cc)
# résultat attendu : [[("e3", Type.PIN_IN), ("d3", Type.FLAG_INPUT)], 
# suite               [("e3", Type.PIN_IN), ("a3", Type.FLAG_INPUT)],
#                     [("e6", Type.PIN_IN), ("d6", Type.HOLE), ("d5", Type.HOLE)], ("e5", Type.PIN_OUT)], 
# suite               [ ("e6", Type.PIN_IN), ("a6", Type.HOLE)], [("n6", Type.GND)]]

print(pin_in_cc)
# résultat attendu :  [("e17", Type.PIN_OUT), ("a17", Type.HOLE), ("a20", Type.HOLE)], ("e20", Type.PIN_OUT)], 

print(pin_in_mb)
# résultat attendu : [[("e15", Type.PIN_IN), ("a15", Type.FLAG_OUTPUT)], 
# suite               [("f17", Type.PIN_IN), ("g17", Type.FLAG_CLOCK)]]

print(pin_out_mb)
# résultat attendu : [[("e17", Type.PIN_OUT), ("c17", Type.FLAG_INPUT)]]

print(pin_out_co)
# résultat attendu : [[("f6", Type.PIN_OUT), ("f4", Type.PIN_IN)], 
# suite               [("f6", Type.PIN_IN), ("f5", Type.PIN_IN)],
# suite               ("f9", Type.PIN_OUT), ("f7", Type.PIN_IN)], 
# suite               [("f9", Type.PIN_IN), ("f8", Type.PIN_IN)]]

g = creation_graphe(circuit_test_flag_out_cc_mb, edges_flag_out_cc_mb)
flag_out_mb = is_pin_in_ok(g)
print(flag_out_mb)
# résultat attendu : [[("f15", Type.PIN_VCC), ("h15", Type.FLAG_OUTPUT)], 
# suite               [("e15", Type.PIN_IN), ("a15", Type.FLAG_OUTPUT)],
#                     [("e21", Type.PIN_GND), ("a21", Type.FLAG_OUTPUT)], 
# suite               [ ("h12", Type.PIN_IN)]]

g = creation_graphe(circuit_test_flag_out_cc_mb, edges_flag_out_cc_mb)
pin_clock_ko = is_pin_clock_ok(g)
print(pin_clock_ko)
# résultat attendu : [[("e12", Type.PIN_CLOCK), ("d12", Type.FLAG_CLOCK)], 
# suite               [("e12", Type.PIN_CLOCK), ("a12", Type.FLAG_CLOCK)]]

