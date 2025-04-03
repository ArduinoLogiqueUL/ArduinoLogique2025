from Noeud import *
import networkx as nx
import re
# from Graphe_Circuit import is_chip_short_circuit, is_chip_sc_gnd_to_pin_vcc_or_pin_out,is_chip_sc_vcc_to_pin_gnd_or_pin_out

# En attendant de transformer les **arg en une liste 
# Fonction pour trouver plusieurs noeuds de meme par example le type VCC
def trouver_noeuds_position(graph, position_recherche):
    noeuds_position_recherche = [position_recherche]
    noeud_position_trouve = [noeud for noeud in graph.nodes if noeud.position in noeuds_position_recherche]
    return noeud_position_trouve

# En attendant de transformer les **arg en une liste 
# Fonction pour trouver plusieurs noeuds de meme par example le type VCC
def trouver_noeuds_type(graph, type_recherche):
    noeuds_types_recherche = [type_recherche]
    noeuds_types_trouves = [noeud for noeud in graph.nodes if noeud.type in noeuds_types_recherche]
    return noeuds_types_trouves

# Fonction pour trouver plusieurs noeuds de deux ou plusieurss par example le type VCC et le type GND
def trouver_noeuds_types(graph, type_recherche, type_recherche_2, **args):
    noeuds_types_recherche = [type_recherche, type_recherche_2]
    noeuds_types_trouves = [noeud for noeud in graph.nodes if noeud.type in noeuds_types_recherche]
    return noeuds_types_trouves

# court circuit 
def is_chip_short_circuit(graph  :nx.Graph):
    # On recupere tous les type.gnd ou type.vcc et on regarde si existe un chemin entre ce type.vcc et le type.gnd
    for n in graph:
        print(n)
    type_vcc= trouver_noeuds_type(graph, Type.VCC)
#    type_gnd= trouver_noeuds_type(graph, Type.GND)
    all_paths_vcc_gnd = []
    
    for n1 in type_vcc:
#        for n2 in type_gnd:
#            if nx.has_path(graph,n1,n2):  
#                all_paths_vcc_gnd.append(list(nx.all_simple_paths(graph, n1, n2)))
                all_paths_vcc_gnd.append(list(nx.all_simple_paths(graph, n1, Type.GND)))
            
#    return list(filter(bool,all_paths_vcc_gnd))
    return list(filter(bool, all_paths_vcc_gnd)) 

def is_chip_sc_vcc_to_pin_gnd_or_pin_out(graph  :nx.Graph):
    # On recupere tous les type.gnd ou type.vcc et on regarde si existe un chemin entre ce type.vcc et le type.gnd
    type_vcc = trouver_noeuds_type(graph, Type.VCC)
    type_pin_gnd_or_pin_output = trouver_noeuds_types(graph, Type.PIN_GND, Type.PIN_OUTPUT)
    vcc_to_pin_gnd_or_pin_out = []
    
    for n1 in type_vcc:
#        for n2 in type_pin_gnd_or_pin_output:
#            if nx.has_path(graph,n1,n2):  
#                vcc_to_pin_gnd_or_pin_out.append(list(nx.all_simple_paths(graph, n1, n2)))
                vcc_to_pin_gnd_or_pin_out.append(list(nx.all_simple_paths(graph, n1, [Type.PIN_GND,Type.PIN_OUTPUT])))
            
#    return list(filter(bool,all_paths_vcc_gnd))
    return list(filter(bool, vcc_to_pin_gnd_or_pin_out))

def is_chip_sc_gnd_to_pin_vcc_or_pin_out(graph  :nx.Graph):
    # On recupere tous les type.gnd ou type.vcc et on regarde si existe un chemin entre ce type.vcc et le type.gnd
    type_gnd = trouver_noeuds_type(graph, Type.GND)
#    type_pin_vcc_or_pin_out = trouver_noeuds_types(graph, Type.PIN_VCC,Type.PIN_OUTPUT)
    gnd_to_pin_vcc_or_pin_out = []
    
    for n1 in type_gnd:
#        for n2 in type_pin_vcc_or_pin_out:
#            if nx.has_path(graph,n1,n2):  
#                gnd_to_pin_vcc_or_pin_out.append(list(nx.all_simple_paths(graph, n1, n2)))
                gnd_to_pin_vcc_or_pin_out.append(list(nx.all_simple_paths(graph, n1, [Type.PIN_VCC,Type.PIN_OUTPUT])))
            
#    return list(filter(bool,all_paths_vcc_gnd))
    return list(filter(bool, gnd_to_pin_vcc_or_pin_out)) 

def find_graph_leaves_types(G: nx.Graph, liste_type_recherche):
    #  """
    # Trouve les nœuds du graphe correspondant à un ou plusieurs types.
    
    # :param graph: Le graphe NetworkX.
    # :param type_recherche: Un type unique ou une liste de types.
    # :param args: Arguments supplémentaires (autres types).
    # :return: Liste des nœuds correspondant aux types recherchés.
    # """
    # recuperer les arguments supplementaires sous forme de liste et list
    ## et s assurer que la liste n est pas vide
    # trouver 
    ## ## list_type_recherche = [type_recherche]
    leaves_types = [node for node in G.nodes if G.degree(node) == 1 and node.type in liste_type_recherche]
        ##print("Feuilles du graphe :", feuilles)
    for leave_type in leaves_types:
        print("Feuille du graphe de type : ", leave_type)

    return leaves_types


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

circuit_test_pin_vcc_gnd_Nopwr_MB = [
                            (Type.FLAG_INPUT,"i21"),(Type.FLAG_OUTPUT,"a27"), (Type.FLAG_CLOCK,"i45"), (Type.FLAG_CLOCK,"b51"),
                            (Type.HOLE,"p33"),(Type.HOLE,"j33"), (Type.HOLE,"i33"), (Type.HOLE,"i34"),
                            (Type.HOLE,"c38"),(Type.HOLE,"c39"), (Type.HOLE,"a39"), (Type.HOLE,"n39"),
                            (Type.PIN_VCC,"f4"), (Type.PIN_INPUT,"f5"),(Type.PIN_INPUT,"f6"),(Type.PIN_OUTPUT,"f7"),
                            (Type.PIN_INPUT,"f8"),(Type.PIN_INPUT,"f9"),(Type.PIN_OUTPUT,"f10"),
                            (Type.PIN_INPUT,"e4"),(Type.PIN_INPUT,"e5"),(Type.PIN_OUTPUT,"e6"),
                            (Type.PIN_INPUT,"e7"),(Type.PIN_INPUT,"e8"),(Type.PIN_OUTPUT,"e9"), (Type.PIN_GND,"e10"), 
                            (Type.PIN_VCC,"f21"), (Type.PIN_INPUT,"f22"),(Type.PIN_INPUT,"f23"),(Type.PIN_OUTPUT,"f24"),
                            (Type.PIN_INPUT,"f25"),(Type.PIN_INPUT,"f26"),(Type.PIN_OUTPUT,"f27"),
                            (Type.PIN_INPUT,"e21"),(Type.PIN_INPUT,"e22"),(Type.PIN_OUTPUT,"e23"),
                            (Type.PIN_INPUT,"e24"),(Type.PIN_INPUT,"e25"),(Type.PIN_OUTPUT,"e26"), (Type.PIN_GND,"e27"), 
                            (Type.PIN_VCC,"f33"), (Type.PIN_INPUT,"f34"),(Type.PIN_INPUT,"f35"),(Type.PIN_OUTPUT,"f36"),
                            (Type.PIN_INPUT,"f37"),(Type.PIN_INPUT,"f38"),(Type.PIN_OUTPUT,"f39"),
                            (Type.PIN_INPUT,"e33"),(Type.PIN_INPUT,"e34"),(Type.PIN_OUTPUT,"e35"),
                            (Type.PIN_INPUT,"e36"),(Type.PIN_INPUT,"e37"),(Type.PIN_OUTPUT,"e38"), (Type.PIN_GND,"e39"), 
                            (Type.PIN_VCC,"f45"), (Type.PIN_INPUT,"f46"),(Type.PIN_INPUT,"f47"),(Type.PIN_OUTPUT,"f48"),
                            (Type.PIN_INPUT,"f49"),(Type.PIN_INPUT,"f50"),(Type.PIN_OUTPUT,"f51"),
                            (Type.PIN_INPUT,"e45"),(Type.PIN_INPUT,"e46"),(Type.PIN_OUTPUT,"e47"),
                            (Type.PIN_INPUT,"e48"),(Type.PIN_INPUT,"e49"),(Type.PIN_OUTPUT,"e50"), (Type.PIN_GND,"e51") 
]  #  à remplir
edges_pin_vcc_gnd_Nopwr_MB = [(27,1),(40,2),(5,6),(6,7), (7,8),(8,42), (53,9),(9,10),
                              (10,54),(10,11),(11,12), (3,55), (68,4)
                              ]   #  à remplir

circuit_test_pin_in_et_pin_out = []  #  à remplir
edges_pin_in_et_pin_out = []   #  à remplir

circuit_test_flag_out_cc_mb = []  #  à remplir
edges_flag_out_cc_mb = []   #  à remplir

circuit_test_pin_clock = []  #  à remplir
edges_pin_clock = []   #  à remplir


def creation_graphe(liste_noeud : list, liste_edge : list) -> nx.Graph:
    noeuds : dict = {}
    G = nx.Graph()
    for i,n in enumerate(liste_noeud):
        t, p = n
        noeuds[str(i+1)] = Noeud( type_= t, position=p, nb_in=2)
        print(f"{i+1} :    {noeuds[str(i+1)]}")
        G.add_node(noeuds[str(i+1)], type = noeuds[str(i+1)].type)
        
    list_edges = [(noeuds[str(e[0])], noeuds[str(e[1])]) for e in liste_edge]
    G.add_edges_from(list_edges)
        
    return G
        
def is_vcc_gnd_in_CC(g : nx.Graph):
    all_paths_0 = is_chip_short_circuit(g)
    print("############# Debut is_chip_short_circuit ############################")
    for path_0 in all_paths_0: 
        print("*****************************************************************")
        for p_0 in path_0: 
            for p0 in p_0:
                print(p0)
    print("############# Fin is_chip_short_circuit ############################")
    all_paths_1 = is_chip_sc_vcc_to_pin_gnd_or_pin_out(g)
    print("############# Debut is_chip_sc_vcc_to_pin_gnd_or_pin_out ############################")
    for paths_1 in all_paths_1: 
        print("*****************************************************************")
        for p_1 in paths_1: 
            for p1 in p_1:
                print(p1)
    print("############# Fin is_chip_sc_vcc_to_pin_gnd_or_pin_out ############################")
    all_paths_2 = is_chip_sc_gnd_to_pin_vcc_or_pin_out(g)
    print("############# Debut is_chip_sc_gnd_to_pin_vcc_or_pin_out ############################")
    for paths_2 in all_paths_2: 
        print("*****************************************************************")
        for p_2 in paths_2: 
            for p2 in p_2:
                print(p2)
    print("############# Fin is_chip_sc_gnd_to_pin_vcc_or_pin_out ############################")
    vcc_to_gnd : list[list[(str, Type)]] = [] # is_chip_short_circuit(g)     
    vcc_to_pin_gnd_or_pin_out : list[list[Noeud]] = [] # is_chip_sc_vcc_to_pin_gnd_or_pin_out(g) 
    gnd_to_pin_vcc_or_pin_out : list[list[Noeud]] = [] # is_chip_sc_gnd_to_pin_vcc_or_pin_out(g) 
    
    return vcc_to_gnd, vcc_to_pin_gnd_or_pin_out, gnd_to_pin_vcc_or_pin_out

## liste_sans_vide = [lst for lst in liste_de_listes if lst]
## liste_sans_vide = list(filter(bool, liste_de_listes))
def all_simple_paths(g,leaves_holes,type_vcc_gnd): ####### 
    list_paths = []
    for leave_hole in leaves_holes:
#        for type_vcc_one in type_vcc:
#            if nx.has_path(g,leave_hole,type_vcc_one):  
#                list_paths.append(list(nx.all_simple_paths(g,leave_hole,type_vcc_one)))
##        list_paths.append(list(nx.all_simple_paths(g,leave_hole,type_vcc_gnd)))
        list_paths.extend(list(nx.all_simple_paths(g,leave_hole,type_vcc_gnd)))
##    return list(filter(bool, list_paths)) ## supprimer les listes vides
    return list_paths ## supprimer les listes vides

def is_vcc_gnd_in_CO(g : nx.Graph):
    
    ## chercher les feuilles qui finissent par hoole
    ## chercher les 
    leaves_holes = find_graph_leaves_types(g, Type.HOLE)

    ## 
##    type_vcc = trouver_noeuds_type(g, Type.VCC)
##    type_gnd = trouver_noeuds_type(g, Type.GND)

    vcc_to_hole_1 = all_simple_paths(g,leaves_holes,Type.VCC)
    gnd_to_hole_1 = all_simple_paths(g,leaves_holes,Type.GND)

    vcc_to_hole : list[list[(str, Type)]]= []
    gnd_to_hole : list[list[(str, Type)]]= []
    
    # à terminer
    
    return vcc_to_hole, gnd_to_hole


def is_vcc_gnd_in_no_pwr_or_MB(g : nx.Graph):
    pin_vcc_gnd_no_pwr : list[(str, Type)] = []
    pin_vcc_gnd_mb :list[list[Noeud]] = [] 
    
    # à terminer    
    ## parcourir les noeuds
        ## chercher les feuilles qui finissent par hoole
    ## chercher les 

    result = []
    ## 
    type_pin_vcc = trouver_noeuds_type(g, Type.PIN_VCC)
    type_pin_gnd = trouver_noeuds_type(g, Type.PIN_GND)

#    types_pin_vcc_gnd = trouver_noeuds_types(g, Type.PIN_VCC,Type.PIN_GND)

###########
############
    for one_pin_vcc in type_pin_vcc:
            result.clear()
            result.extend(list(nx.all_simple_paths(g,one_pin_vcc,Type.VCC)))
            if not result: # liste vide ajout aux deux listes 

######### HOLE Niveau1 = no_pwr
                pin_vcc_gnd_no_pwr.append(result) 
                pin_vcc_gnd_mb.append(result)
            # elif result: ## all hole 
            #     pin_vcc_gnd_no_pwr_1.append(one_pin_vcc_gnd)
            # else:## liste non vide avec elements avec hole et autres
            #     pin_vcc_gnd_mb_1.append(one_pin_vcc_gnd) 

    for one_pin_gnd in type_pin_gnd:
            result.clear()
            result.extend(list(nx.all_simple_paths(g,one_pin_gnd,Type.GND)))
            if not result: # liste vide 
                pin_vcc_gnd_no_pwr.append(one_pin_gnd) 
                pin_vcc_gnd_mb.append(one_pin_gnd)
            # elif result: ## all hole 
            #     pin_vcc_gnd_no_pwr_1.append(one_pin_vcc_gnd)
            # else:## liste non vide avec elements avec hole et autres
            #     pin_vcc_gnd_mb_1.append(one_pin_vcc_gnd)  
   
    return pin_vcc_gnd_no_pwr, pin_vcc_gnd_mb

def is_pin_in_cc(g : nx.Graph):
    # à terminer avec ce principe:
    # il y a CC si une pin_in est connecter à plus d'un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    # il y a CC si une pin_in est connecter à un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    pin_in_cc_1 : list[list[Noeud]]= []

    types_pin_in = trouver_noeuds_type(g, Type.PIN_INPUT)
    for one_pin_in in types_pin_in:

#       if (nx.has_path(g,one_pin_in,Type.VCC)):              
        pin_in_cc_1.extend(list(nx.all_simple_paths(g,one_pin_in,[Type.VCC,Type.GND, Type.PIN_OUTPUT,Type.FLAG_INPUT])))
        ## on supprime les elements vides de la listes
#        nb_result_non_vides = len(list(filter(bool, result))) ## supprimer les listes vides
        # if(len(list(filter(bool, result))))>1:
        #     pin_in_cc_1.append(one_pin_in) 

    return pin_in_cc_1

# il y a CC si une pin_out est connecter à plus d'un de ces choix:  FLAG_OUTPUT
def is_pin_out_cc(g : nx.Graph):
    # à terminer avec ce principe:
    # il y a CC si une pin_out est connecter à un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT ou PIN_INPUT
    pin_out_cc_1 : list[list[Noeud]]= []
    result = []
    result_sans_vides = []
    types_pin_out = trouver_noeuds_type(g, Type.PIN_OUTPUT)
    for one_pin_out in types_pin_out:
        result.clear()
        result_sans_vides.clear()
#       if (nx.has_path(g,one_pin_in,Type.VCC)):              
        pin_out_cc_1.extend(list(nx.all_simple_paths(g,one_pin_out,[Type.VCC,Type.GND, Type.PIN_OUTPUT,Type.PIN_INPUT,Type.FLAG_INPUT,Type.PIN_CLOCK])))
        ## on supprime les elements vides de la listes
#        nb_result_non_vides = len(list(filter(bool, result))) ## supprimer les listes vides
#        # if(len(list(filter(bool, result))))>0:
#        #     pin_out_cc_1.append(one_pin_out) 

    return pin_out_cc_1


def is_pin_in_mb(g : nx.Graph):
# il y a mauvais branchement mb si une pin_in est connectée à : FLAG_OUTPUT ou FLAG_CLOCK    
    pin_in_mb_1 :list[list[Noeud]]= []  
    result = []
    result_sans_vides = []
    types_pin_input = trouver_noeuds_type(g, Type.PIN_INPUT)
    for one_pin_input in types_pin_input:
        result.clear()
        result_sans_vides.clear()
#       if (nx.has_path(g,one_pin_in,Type.VCC)):              
        pin_in_mb_1.extend(list(nx.all_simple_paths(g,one_pin_input,[Type.FLAG_OUTPUT,Type.FLAG_CLOCK])))
        ## on supprime les elements vides de la listes
#        nb_result_non_vides = len(list(filter(bool, result))) ## supprimer les listes vides
###        if(len(list(filter(bool, result))))>0:
###            pin_in_mb_1.append(one_pin_input) 

    return pin_in_mb_1

def is_pin_out_mb(g : nx.Graph):
# il y a mauvais branchement mb si une pin_out est connectée à : FLAG_INPUT ou FLAG_CLOCK    
    pin_out_mb_1 :list[list[Noeud]]= [] 
    result = []
    result_sans_vides = []
    types_pin_out = trouver_noeuds_type(g, Type.PIN_OUTPUT)
    for one_pin_out in types_pin_out:
        result.clear()
        result_sans_vides.clear()  
        pin_out_mb_1.extend(list(nx.all_simple_paths(g,one_pin_out,[Type.FLAG_INPUT,Type.FLAG_CLOCK])))
        ## on supprime les elements vides de la listes
#        nb_result_non_vides = len(list(filter(bool, result))) ## supprimer les listes vides
#        # if(len(list(filter(bool, result))))>0:
#        #     pin_out_mb_1.append(one_pin_out) 

    return pin_out_mb_1

def is_pin_out_co(g : nx.Graph):
# il y a co si une pin_out a au moins une de ses entrées non connectée, si aucune entrée n'est connectée
# Il y a aussi co si un pin_out n'est pas connecté et qu'il y a au moins une entrée active.

# associer les pins input associes aux pins output
    pin_out_co_1 :list[Noeud] = []
    types_pin_out :list[Noeud] = []
    result :list[Noeud] = []
    
    types_pin_out = trouver_noeuds_type(g, Type.PIN_OUTPUT)
    for one_pin_out in types_pin_out: ## le trouver les pins input et output associes au pin.vcc du composant    
        result.clear() 
        result.extend(list(nx.all_simple_paths(g,one_pin_out,Type.PIN_INPUT)))  
        if (len(pin_out_co_1))>= one_pin_out.nb_in: ## pin en co
            pin_out_co_1.extend(result)

    return pin_out_co_1


## le dernier a encoder
def is_pin_in_ok(g : nx.Graph):
    pin_in_cc : list[list[Noeud]]= [] 
    pin_out_cc :list[list[Noeud]]= [] 
    pin_in_mb :list[list[Noeud]]= [] 
    pin_out_mb :list[list[Noeud]]= [] 
    pin_out_co :list[list[Noeud]]= [] 

    # à terminer avec ce principe:
    # il y a CC si une pin_in est connecter à plus d'un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    # il y a CC si une pin_in est connecter à un de ces choix: PIN_OUT ou VCC ou GND ou FLAG_INPUT
    pin_in_cc = is_pin_in_cc(g)

    # il y a CC si une pin_out est connecter à plus d'un de ces choix:  FLAG_OUTPUT
    pin_out_cc = is_pin_out_cc(g)

    # il y a mauvais branchement mb si une pin_in est connectée à : FLAG_OUTPUT ou FLAG_CLOCK
    pin_in_mb = is_pin_in_mb(g)

    # il y a mauvais branchement mb si une pin_out est connectée à : FLAG_INPUT ou FLAG_CLOCK
    pin_out_mb = is_pin_out_mb(g)

    # il y a co si une pin_out a au moins une de ses entrées non connectée, si aucune entrée n'est connectée
    # Il y a aussi co si un pin_out n'est pas connecté et qu'il y a au moins une entrée active.
    pin_out_co = is_pin_out_co(g)

    # on a un état nc qui n'est pas bloquant. La propriété _nb_in contient le nombre d'entrées d'un pin_out
    return pin_in_cc, pin_out_cc, pin_in_mb, pin_out_mb, pin_out_co

## si poser si une entree non connecte ie seules 
def is_flag_out_mb(g :nx.Graph):
    flag_out_mb :list[list[Noeud]]  = [] 
    types_flag_out :list[Noeud] = []
    
    types_flag_out = trouver_noeuds_type(g, Type.FLAG_OUTPUT)
    for one_flag_out in types_flag_out: ## le trouver les pins input et output associes au pin.vcc du composant    
        flag_out_mb.extend(list(nx.all_simple_paths(g,one_flag_out,Type.PIN_OUTPUT)))                                                                   
    
    return flag_out_mb

## pin_clock_avec flag_clok
def is_pin_clock_ok(g :nx.Graph):
    pin_clock_ko :list[list[Noeud]]= [] 
    types_pin_clock :list[Noeud] = []
    
    types_pin_clock = trouver_noeuds_type(g, Type.PIN_CLOCK)
    for one_pin_clock in types_pin_clock: ## le trouver les pins input et output associes au pin.vcc du composant    
        pin_clock_ko.extend(list(nx.all_simple_paths(g,one_pin_clock,Type.FLAG_CLOCK)))  

    return pin_clock_ko


g_0 = creation_graphe(circuit_test_vcc_gnd_cc, edges_vcc_gnd)
for n in g_0:
     print(n)

vcc_to_gnd, vcc_to_pin_gnd_or_pin_out, gnd_to_pin_vcc_or_pin_out = is_vcc_gnd_in_CC(g_0)
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

vcc_to_hole, gnd_to_hole = is_vcc_gnd_in_CO(g_0)
print(vcc_to_hole)
# résultat attendu : [[("p42", Type.VCC), ("i42", Type.HOLE)]] 
print(gnd_to_hole)
# résultat attendu : [[("n48", Type.GND), ("j48", Type.HOLE), ("h48", Type.HOLE), ("h54", Type.HOLE), ("i54", Type.HOLE), ("i57", Type.HOLE),
# suite                ("g57", Type.HOLE), ("c57", Type.HOLE), ("b57", Type.HOLE), ("b51", Type.HOLE)]] 

g_1 = creation_graphe(circuit_test_pin_vcc_gnd_Nopwr_MB, edges_pin_vcc_gnd_Nopwr_MB)
pin_vcc_gnd_no_pwr, pin_vcc_gnd_mb = is_vcc_gnd_in_no_pwr_or_MB(g_1)
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

g_2 = creation_graphe(circuit_test_pin_in_et_pin_out, edges_pin_in_et_pin_out)
pin_in_cc, pin_out_cc, pin_in_mb, pin_out_mb, pin_out_co = is_pin_in_ok(g_2)
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

g_3 = creation_graphe(circuit_test_flag_out_cc_mb, edges_flag_out_cc_mb)
flag_out_mb = is_pin_in_ok(g_3)
print(flag_out_mb)
# résultat attendu : [[("f15", Type.PIN_VCC), ("h15", Type.FLAG_OUTPUT)], 
# suite               [("e15", Type.PIN_IN), ("a15", Type.FLAG_OUTPUT)],
#                     [("e21", Type.PIN_GND), ("a21", Type.FLAG_OUTPUT)], 
# suite               [ ("h12", Type.PIN_IN)]]

g_4 = creation_graphe(circuit_test_flag_out_cc_mb, edges_flag_out_cc_mb)
pin_clock_ko = is_pin_clock_ok(g_4)
print(pin_clock_ko)
# résultat attendu : [[("e12", Type.PIN_CLOCK), ("d12", Type.FLAG_CLOCK)], 
# suite               [("e12", Type.PIN_CLOCK), ("a12", Type.FLAG_CLOCK)]]

