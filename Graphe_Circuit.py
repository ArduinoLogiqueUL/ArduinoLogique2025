import networkx as nx
import Noeud
from Noeud import Noeud, Type

def add_nodes_circuit(graph  :nx.Graph): # entre tous les noeuds du circuit

## G.add_nodes_from([(n1,type=n1.type), (n2,type=n2.type)])
## Tester mauvais branchement des pins.vcc avec Type.GND  
    n1 = Noeud(type_= Type.VCC, position = "p4")
    G.add_node(n1,type=n1.type)
#    n1 = Noeud(type_= Type.GND, position = "n4")
#    G.add_node(n1,type=n1.type)
    n2 = Noeud(type_= Type.HOLE, position = "h4")
    G.add_node(n2,type=n2.type)
###    G.add_nodes_from([(n1,type=n1.type), (n2,type=n2.type)])
    #G.add_edge(n1,n2)
    n3 = Noeud(type_= Type.HOLE, position = "g4")
    G.add_node(n3,type=n3.type)
    n4 = Noeud(type_= Type.HOLE, position = "g7")
    G.add_node(n4,type=n4.type)

#    n = Noeud(type_= Type.GND, position = "n3") # erreur sommet isole
#    G.add_node(n,type=n.type)

    # n5 = Noeud.Noeud(type_= Noeud.Type.PIN_INPUT, position = "e7")
    n5 = Noeud(type_= Type.PIN_VCC, position = "f7")
    G.add_node(n5,type=n5.type)
    #Ajouter un fil d13 et d15
    n6 = Noeud(type_= Type.HOLE, position = "d13")
    G.add_node(n6,type=n6.type)
    n7 = Noeud(type_= Type.HOLE, position = "d15")
    G.add_node(n7,type=n7.type)

    #Ajouter un fil e15 et un ground n15
    n8 = Noeud(type_= Type.HOLE, position = "e15")
    G.add_node(n8,type=n8.type)
#   Tester la pin.GND fonctionnel puis tester erreur avec p15 sur pin.GND 
#    n9 = Noeud(type_= Type.GND, position = "n15")  ## OK OK OK TESTE
    # Tester erreur avec n15 : remplace par p15 donc pin.GND alimente par VCC
    n9 = Noeud(type_= Type.VCC, position = "p15")
    G.add_node(n9,type=n9.type)

    n10 = Noeud(type_= Type.PIN_GND, position = "e13") #e13 avec d13 connection par la plaque
    G.add_node(n10,type=n10.type)

# ajouter ces deux noeuds fictifs pour eviter exception lors de la recherche
    n11 = Noeud(type_= Type.GND, position = "n45") # ajouter ces deux noeuds fictifs pour eviter exception lors de la recherche
    G.add_node(n11,type=n11.type)
    n12 = Noeud(type_= Type.VCC, position = "p47") # ajouter ces deux noeuds fictifs pour eviter exception lors de la recherche
    G.add_node(n12,type=n12.type)

################### TESTS COURT CIRCUIT DIRECT p10 et n10 et edge(n13,n14) #########################
    n13 = Noeud(type_= Type.VCC, position = "p10") 
    G.add_node(n13,type=n13.type)
    n14 = Noeud(type_= Type.GND, position = "n10") 
    G.add_node(n14,type=n14.type)
################### FIN TESTS COURT CIRCUIT DIRECT p10 et n10 ######################
################### TESTS COURT CIRCUIT CIRCUIT INDIRECTE (p35 et h35) (g35 et g40) (h40 et n40) #########################
    n15 = Noeud(type_= Type.VCC, position = "p35") 
    G.add_node(n15,type=n15.type)
    n16 = Noeud(type_= Type.HOLE, position = "h35") 
    G.add_node(n16,type=n16.type)
    n17 = Noeud(type_= Type.HOLE, position = "g35") 
    G.add_node(n17,type=n17.type)
    n18 = Noeud(type_= Type.HOLE, position = "g40") 
    G.add_node(n18,type=n18.type)
    n19 = Noeud(type_= Type.HOLE, position = "h40") 
    G.add_node(n19,type=n19.type)
    n20 = Noeud(type_= Type.GND, position = "n40") 
    G.add_node(n20,type=n20.type)
################### FIN TESTS COURT CIRCUIT INDIRECTE p35 et h35 ######################

################### DEBUT  TESTS CIRCUIT OUVERT (p19, g19) (f19,c19) (b19, b30) (c30, h30)(a30, a36) ######################
    # n21 = Noeud(type_= Type.VCC, position = "p19") 
    # G.add_node(n21,type=n21.type)
    n21 = Noeud(type_= Type.VCC, position = "n19") 
    G.add_node(n21,type=n21.type)
    n22 = Noeud(type_= Type.HOLE, position = "g19") 
    G.add_node(n22,type=n22.type)
    n23 = Noeud(type_= Type.HOLE, position = "f19") 
    G.add_node(n23,type=n23.type)
    n24 = Noeud(type_= Type.HOLE, position = "c19") 
    G.add_node(n24,type=n24.type)
    n25 = Noeud(type_= Type.HOLE, position = "b19") 
    G.add_node(n25,type=n25.type)
    n26 = Noeud(type_= Type.HOLE, position = "b30") 
    G.add_node(n26,type=n26.type)
    n27 = Noeud(type_= Type.HOLE, position = "c30") 
    G.add_node(n27,type=n27.type)
    n28 = Noeud(type_= Type.HOLE, position = "h30") 
    G.add_node(n28,type=n28.type)

################### FIN  TESTS CIRCUIT OUVERT (p19, g19) (f19,c19) (b19, b30) (c30, h30) ######################

################### DEBUT  TESTS FLAGS (e7 input: fonc=NAND_1, e8 input: fonc=NAND_1, e9 output: fonc=NAND_1) (d7 flag input, d8 flag input, d9 flag output) ######################
################### AJOUTER DES FONCTIONS ###################################################################
    n29 = Noeud(type_= Type.PIN_INPUT, position = "e7", func = "NAND_1")
    G.add_node(n29,type=n29.type)
    n30 = Noeud(type_= Type.PIN_INPUT, position = "e8", func = "NAND_1")
    G.add_node(n30,type=n30.type)
    n31 = Noeud(type_= Type.PIN_OUTPUT, position = "e9", func = "NAND_1") # chaque fonction nand_1 est etiqueter puis executer de la meme facon
    G.add_node(n31,type=n31.type)
    ################### FLAGS (d7 flag input, d8 flag input, d9 flag output) ###########################
    n32 = Noeud(type_= Type.FLAG_INPUT, position = "d7", func = "NAND_1")
    G.add_node(n32,type=n32.type)
    n33 = Noeud(type_= Type.FLAG_INPUT, position = "d8", func = "NAND_1")
    G.add_node(n33,type=n33.type)
    n34 = Noeud(type_= Type.FLAG_OUTPUT, position = "d9", func = "NAND_1") # chaque fonction nand_1 est etiqueter puis executer de la meme facon
    G.add_node(n34,type=n34.type)
    n35 = Noeud(type_= Type.HOLE, position = "a30")
    G.add_node(n35,type=n35.type)
    n36 = Noeud(type_= Type.HOLE, position = "a36") # chaque fonction nand_1 est etiqueter puis executer de la meme facon
    G.add_node(n36,type=n36.type)
#################### AJOUT VCC ou GND sur le input e7 ##########################
    n37 = Noeud(type_= Type.HOLE, position = "a7")
    G.add_node(n37,type=n37.type)
    n38 = Noeud(type_= Type.HOLE, position = "a3") # chaque fonction nand_1 est etiqueter puis executer de la meme facon
    G.add_node(n38,type=n38.type)
    n39 = Noeud(type_= Type.HOLE, position = "b3")
    G.add_node(n39,type=n39.type)
    n40 = Noeud(type_= Type.VCC, position = "p3") # chaque fonction nand_1 est etiqueter puis executer de la meme facon
    G.add_node(n40,type=n40.type)


################### FIN  TESTS FLAGS (e7 input: fonc=NAND_1, e8 input: fonc=NAND_1, e9 output: fonc=NAND_1) (d7 flag input, d8 flag input, d9 flag output) ######################

    G.add_edges_from([(n1,n2), (n2,n3), (n3,n4), (n4,n5), (n6,n7), (n8,n9), (n10,n6), (n7,n8), (n13,n14), (n15,n16), 
                      (n17,n18), (n19,n20), (n16,n17), (n18,n19), (n21,n22), (n23,n24), (n25,n26), 
                      (n27,n28), (n22,n23),(n24,n25), (n26,n27), (n29,n32), (n30,n33),(n31,n34), (n35,n36),(n26, n35),
                      (n37,n38),(n39, n40), (n32,n37),(n38, n39)])
    # (n7,n8) #d15 et e15
   
    n = Noeud(type_= Type.PIN_INPUT, position = "e10")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_INPUT, position = "e11")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_OUTPUT, position = "e12", func = "NAND")
    G.add_node(n,type=n.type)
    # n = Noeud(type_= Type.PIN_GND, position = "e13")
    # G.add_node(n,type=n.type)
    # n = Noeud.Noeud(type_= Noeud.Type.PIN_VCC, position = "f7")
    n = Noeud(type_= Type.PIN_INPUT, position = "e7")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_INPUT, position = "f8")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_INPUT, position = "f9")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_OUTPUT, position = "f10", func = "NAND")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_INPUT, position = "f11")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_INPUT, position = "f12")
    G.add_node(n,type=n.type)
    n = Noeud(type_= Type.PIN_OUTPUT, position = "f13", func = "NAND")
    G.add_node(n,type=n.type)

# Fonction pour trouver un nœud de type VCC
# def trouver_noeud_type(graph, type_recherche):
#     for noeud in graph.nodes:
#         if noeud.type == type_recherche:
#             return noeud
#     return None

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

def is_chip_powered(graph  :nx.Graph):
#    pin_vcc_gnd = [n for n in graph.nodes if n.type in [Noeud.Type.PIN_VCC, Noeud.Type.PIN_GND]]
    pin_vcc_gnd = trouver_noeuds_types(graph, Type.PIN_VCC, Type.PIN_GND)
    connected=[]
    not_connected=[]

    for n in pin_vcc_gnd:
        if n.type == Type.PIN_VCC:
            if nx.has_path(G,n,Type.VCC):  
                connected.append(n)
            else:
                not_connected.append(n)
        else: # n.type == Noeud.Type.PIN_GND:
            if nx.has_path(G,n,Type.GND):  
                connected.append(n)
            else:
                not_connected.append(n)

    return (connected,not_connected)

def is_chip_bad_powered(graph  :nx.Graph):
#    pin_vcc_gnd = [n for n in graph.nodes if n.type in [Noeud.Type.PIN_VCC, Noeud.Type.PIN_GND]]
    # On recupere les pins.gnd et pin.vcc
    pin_vcc_gnd = trouver_noeuds_types(graph, Type.PIN_VCC, Type.PIN_GND)
    bad_connected=[]

    for n in pin_vcc_gnd:
        if n.type == Type.PIN_VCC:
            if nx.has_path(G,n,Type.GND):  
                bad_connected.append(n)
        else: # n.type == Noeud.Type.PIN_GND:
            if nx.has_path(G,n,Type.VCC):  
                bad_connected.append(n)

    return (bad_connected)

# # court circuit 
# def is_chip_short_circuit(graph  :nx.Graph):
#     # On recupere tous les type.gnd ou type.vcc et on regarde si existe un chemin entre ce type.vcc et le type.gnd
#     type_vcc_gnd= trouver_noeuds_types(graph, Type.VCC, Type.GND)
#     all_paths_vcc_gnd = []
# #    all_paths = list(nx.all_simple_paths(graph, Type.VCC, Type.GND))

#     for n in type_vcc_gnd:
# #         if nx.has_path(G,n,Type.GND):  
# #             short_path = nx.shortest_path(G, n, Type.GND)
# # #           for un_chemin in path:
#         if(n.type in [Type.VCC]):
# #             # Trouver tous les chemins entre A et D
#             all_paths_vcc_gnd.append(list(nx.all_simple_paths(graph, n, Type.GND)))
#         else:#Type.GND
#             all_paths_vcc_gnd.append(list(nx.all_simple_paths(graph, n, Type.VCC)))

#     # print(f"\n✅ Plus court chemin :")
#     # print(f" ====> ".join([str(noeud) for noeud in short_path]))

#     # print(f"\n✅ Tous les chemins possibles :")
#     # for un_chemin in all_paths:
#     #     print(f" ===> ".join([str(one_path) for one_path in un_chemin]))


#     return list(filter(bool,all_paths_vcc_gnd))

# court circuit 
def is_chip_short_circuit(graph  :nx.Graph):
    # On recupere tous les type.gnd ou type.vcc et on regarde si existe un chemin entre ce type.vcc et le type.gnd
    type_vcc= trouver_noeuds_type(graph, Type.VCC)
    type_gnd= trouver_noeuds_type(graph, Type.GND)
    all_paths_vcc_gnd = []
    
    for n1 in type_vcc:
        for n2 in type_gnd:
            if nx.has_path(G,n1,n2):  
                all_paths_vcc_gnd.append(list(nx.all_simple_paths(graph, n1, n2)))
            
#    return list(filter(bool,all_paths_vcc_gnd))
    return all_paths_vcc_gnd


# court circuit 
# def is_chip_open_circuit(graph  :nx.Graph):
#     # On recupere tous les type.gnd et ensuite  type.vcc 
#     # et on regarde s'il n'existe pas un chemin entre ce type.vcc et le type.gnd
#     # et inversement
#     ## open_circuit avec depart vers vcc et aussi depart vers gnd a faire 
#     type_vcc= trouver_noeuds_type(graph, Type.VCC)
#     all_paths_vcc_gnd_pin_gnd = []
#     all_paths_vcc_possible = []
#     chemins_without_gnd = []
#     # for n in type_vcc:
#     #     all_paths_vcc_gnd_pin_gnd.append(list(nx.all_simple_paths(graph, n, Type.GND)))
#     # for n in type_vcc:
#     #     all_paths_vcc_gnd_pin_gnd.append(list(nx.all_simple_paths(graph, n, Type.PIN_GND)))
#     lgn = [n.type for n in G.nodes if n.type != Type.GND]
#     for n in type_vcc:
#         all_paths_vcc_possible.append(list(nx.all_simple_paths(graph, n, target = all))) ## tous les chemins partant du vcc possible
#     ## filter les circuits ouverts 
#     # Filtrer ceux qui se terminent par GND ou VCC
#     chemins_without_gnd = [chemin for chemin in all_paths_vcc_possible if chemin[-1] not in [Type.GND, Type.PIN_GND]]
# #    return list(filter(bool,chemins_without_gnd))
#     return chemins_without_gnd

# def is_chip_open_circuit(graph: nx.Graph):
#     """
#     Détecte un circuit ouvert en recherchant les chemins partant de VCC
#     qui ne se terminent pas par GND ou PIN_GND.
#     """
#     type_vcc = trouver_noeuds_type(graph, Type.VCC)  # Trouve les nœuds VCC
#     all_paths_vcc_possible = []  # Liste de tous les chemins depuis VCC
#     chemins_without_gnd = []  # Liste des chemins ouverts (sans GND)

#     for n in type_vcc:
#         # Récupère tous les chemins simples partant de VCC
#         for target in graph.nodes:  # Teste chaque nœud comme cible possible
#             if target != n:  # Évite de prendre le nœud lui-même
#                 try:
#                     paths = list(nx.all_simple_paths(graph, source=n, target=target))
#                     all_paths_vcc_possible.extend(paths)  # Ajoute les chemins trouvés
#                 except nx.NetworkXNoPath:
#                     pass  # Ignore les erreurs s'il n'y a pas de chemin

#     # Filtrer les chemins qui ne se terminent PAS par GND ou PIN_GND
#     chemins_without_gnd = [chemin for chemin in all_paths_vcc_possible if chemin[-1] not in [Type.GND, Type.PIN_GND]]

#     return chemins_without_gnd


# def detect_short_circuits(graph):
#     """
#     Détecte la présence d'un court-circuit entre VCC et GND.
#     """
#     if nx.has_path(graph, "VCC", "GND"):
#         paths = list(nx.all_shortest_paths(graph, "VCC", "GND"))
#         for path in paths:
#             node_types = [graph.nodes[node]["type"] for node in path[1:-1] if "type" in graph.nodes[node]]
#             if all(nt not in ["INPUT", "OUTPUT", "CLOCK"] for nt in node_types):  # Un chemin direct sans composant autres
#                 print(f"⚠️ Court-circuit détecté entre VCC et GND via {path}")
#                 return
#     print("✅ Aucun court-circuit détecté.")


def find_graph_leaves(G: nx.Graph):
    # trouver 
    leaves = [node for node in G.nodes if G.degree(node) == 1]
        ##print("Feuilles du graphe :", feuilles)
    for leave in leaves:
        print("Feuille du graphe :", leave)

    return leaves
## pour le moment deux fonctions: a regrouper apres tests si plus 
## de performance ou de 

def find_graph_leaves_types(G: nx.Graph, type_recherche):
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
    leaves_types = [node for node in G.nodes if G.degree(node) == 1 and node.type in type_recherche]
        ##print("Feuilles du graphe :", feuilles)
    for leave_type in leaves_types:
        print("Feuille du graphe de type : ", leave_type)

    return leaves_types


def is_chip_open_circuit(graph: nx.Graph):
    """
    Détecte un circuit ouvert en recherchant les chemins partant de VCC
    qui ne se terminent pas par GND ou PIN_GND.
    """
    type_vcc_gnd = trouver_noeuds_types(graph, Type.VCC, Type.GND)  # Trouve les nœuds VCC


    all_paths_vcc_gnd_in_open_circuit = []  # Liste de tous les chemins depuis VCC
    chemins_without_gnd = []  # Liste des chemins ouverts (sans GND)

    leaves = find_graph_leaves(graph)
    leaves_without_vcc_gnd = [lv for lv in leaves if lv.type not in [Type.VCC, Type.GND, Type.PIN_GND, Type.PIN_VCC]]
    # on parcourt chaque feuille et s'il n'est pas de type vcc, gnd, pin_vcc ou pin_gnd  
    ## pour chaque noeud de type vcc ou gnd 
    for n in type_vcc_gnd:
##        for one_leave in leaves:  # on parcourt chaque feuille            
#            if nx.has_path(G,n,leaves_without_vcc_gnd): # s<il existe un chemin entre la feuille et le vcc                    
##                    try:
                    paths = list(nx.all_simple_paths(graph, source=n, target=leaves_without_vcc_gnd))
                    all_paths_vcc_gnd_in_open_circuit.extend(paths)  # Ajoute les chemins trouvés
##                    except nx.NetworkXNoPath:
##                        pass  # Ignore les erreurs s'il n'y a pas de chemin
    return all_paths_vcc_gnd_in_open_circuit

## Fonction flags sortie avec ouput d9 sans input (0) : CO 
## et la meme fonction : 2 flags input qui ferment le circuit,
## 2 entree sans output alors CO:
def is_chip_flags(graph: nx.Graph, type_recherche, **kargs):
    ## recupere les pins input et output dans deux listes differentes :
    ## pour chaque pin output on trouve les deux input associes 
    ## puis proceder aux tests de validation
    ## etude de cas de chaque situation 
    # Convertir en liste et ajouter les types supplémentaires
    types_voulu = [type_recherche] + list(kargs.values()) 
    leaves_types = find_graph_leaves_types(graph, types_voulu)
    ## associer deux pin_input avec un pin_output
    ## 
    return leaves_types


# Création du graphe de noeuds 
G = nx.Graph()
print(type(G))
add_nodes_circuit(G)
connected, not_connected = is_chip_powered(G)
print("***************Les pins connectes***************************")
for n in connected:
    print(n)
print("***************Les pins non connectes***************************")
for n in not_connected:
    print(n)

################ bad connected #################################
bad_connected = is_chip_bad_powered(G)
print("***************Les pins gnd et pin vcc bad connectes***************************")
#print("***************Les pins gnd et pin vcc bad connectes***************************")
for n in bad_connected:
    print(n)
#shortest_path, all_paths = is_chip_short_circuit(G)
all_paths = is_chip_short_circuit(G)
for p in all_paths:
    print(p)

all_open_circuit = is_chip_open_circuit(G)
for p in all_open_circuit:
    print(p)

leaves_types_input = is_chip_flags(G, Type.PIN_INPUT)
for leave_type_input in leaves_types_input:
    print(leave_type_input)

leaves_types_ouput = is_chip_flags(G, Type.PIN_OUTPUT)
## on parcourt la liste des output et on retrouve les deux input associes
## en passant par la fonction func_id
##############################################
# i : int  = 0
# liste_de_listes = []
# for leave_type_output in leaves_types_ouput:       
#     print(leave_type_output)
#     sous_liste = []
#     sous_liste.append(leave_type_output)
#     for leave_type_input in leaves_types_input:
#         print(leave_type_input)        
#         if (leave_type_output.func_id == leave_type_input.func_id): ## ils ont la meme fonction 
#             sous_liste.append(leave_type_input)
#     liste_de_listes.append(sous_liste)
# print(liste_de_listes)
###################################

## a decouper en petites fonction qpour all_simple_paths pour analyser et conclure 
## 
#########################################
# for sous_list in liste_de_listes:
#     ## on parcourt chaque element de la liste et  
#     n_input = len([n for n in sous_list if n.type == Type.PIN_INPUT])
#     j : int = 0
#     if nx.has_path(G,sous_list[j],Type.FLAG_OUTPUT):        
#         if nx.has_path(G,sous_list[j+1],Type.FLAG_INPUT):
#             if nx.has_path(G,sous_list[j+2],Type.FLAG_INPUT):
#                 print("Bon brachement des 3 pins sur le noeuds : {sous_list[j]} {sous_list[j+1]} {sous_list[j+2]}")
#             elif nx.has_path(G,sous_list[j+2],Type.FLAG_OUTPUT): ## Type.FLAG_OUTPUT
#                 print("Mauvais branchement du Type.FLAG_OUTPUT sur le noeud : {sous_list[j+2]}")
#             elif nx.has_path(G,sous_list[j+2],Type.FLAG_CLOCK): ## Type.FLAG_CLOCK
#                 print("Mauvais branchement du Type.FLAG_CLOCK sur le noeud : {sous_list[j+2]}")
#             elif nx.has_path(G,sous_list[j+2],Type.VCC): ## Type.Type.VCC
#                 print("Mauvais branchement du pin avec le Type.VCC sur le noeud : {sous_list[j+2]}")
#             elif nx.has_path(G,sous_list[j+2],Type.GND): ## Type.GND
#                 print("Mauvais branchement du pin avec le Type.GND sur le noeud : {sous_list[j+2]}")
#             else: ## noeud non connecter
#                 print("Le noeud : {sous_list[j+2]} n'est pas connecte ou mauvaise connection") ## type void, hole, etc
#         elif nx.has_path(G,sous_list[j+1],Type.FLAG_OUTPUT):
#                 print("Mauvais branchement du Type.FLAG_OUTPUT sur le noeud : {sous_list[j+1]}")
#         elif nx.has_path(G,sous_list[j+1],Type.FLAG_CLOCK):
#                 print("Mauvais branchement du Type.FLAG_CLOCK sur le noeud : {sous_list[j+1]}")
#         elif nx.has_path(G,sous_list[j+1],Type.GND):
#                 print("Mauvais branchement du Type.Type.GND sur le noeud : {sous_list[j+1]}")
#         elif nx.has_path(G,sous_list[j+1],Type.VCC):
#                 print("Mauvais branchement du Type.Type.VCC sur le noeud : {sous_list[j+1]}")
#         else: ## noeud non connecter
#                 print("Le noeud : {sous_list[j+1]} n'est pas connecte ou mauvaise connection")## type void, hole, etc
#     elif nx.has_path(G,sous_list[j],Type.FLAG_INPUT):   
#         print("Mauvais branchement du Type.FLAG_INPUT sur le noeud : {sous_list[j]}")
#     elif nx.has_path(G,sous_list[j],Type.FLAG_CLOCK):   
#         print("Mauvais branchement du Type.FLAG_INPUT sur le noeud : {sous_list[j]}")
#     elif nx.has_path(G,sous_list[j],Type.FLAG_CLOCK):   
#         print("Mauvais branchement du Type.FLAG_INPUT sur le noeud : {sous_list[j]}")
#     elif nx.has_path(G,sous_list[j],Type.GND):   
#         print("Mauvais branchement du Type.GND sur le noeud : {sous_list[j]}")
#     elif nx.has_path(G,sous_list[j],Type.VCC):   
#         print("Mauvais branchement du Type.VCC sur le noeud : {sous_list[j]}")
#     else:   
#         print("Le noeud : {sous_list[j]} n'est pas connecte ou mauvaise connection")## type void, hole, etc
#####################################################################
#############################################################
############# CONNECTION ###################################
#n29 = Noeud(type_= Type.PIN_INPUT, position = "e7", func = "NAND_1")

# Rechercher les nœuds de type "LED"
# led_nodes = [node for node, data in G.nodes(data=True) if data.type == Type.PIN_INPUT and data.position == "e7"]

#print(f"Nœuds de Type.INPUT : {led_nodes}")
 
reachable_nodes = nx.node_connected_component(G, n)
leaves = find_graph_leaves(G)
leaves_without_vcc_gnd = [lv for lv in leaves if lv.type not in [Type.VCC, Type.GND, Type.PIN_GND, Type.PIN_VCC]]

exists = any(leaf in reachable_nodes for leaf in leaves_without_vcc_gnd)
print(f"Un chemin existe vers au moins un nœud de leaves_without_vcc_gnd ? {exists}")



