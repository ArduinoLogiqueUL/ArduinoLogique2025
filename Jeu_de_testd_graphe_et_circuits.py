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

