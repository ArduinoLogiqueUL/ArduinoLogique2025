import networkx as nx
import re  # Importation du module regex
##########################################################################
#                CREATION DE LA CLASSE COMPOSANT                         #
##########################################################################
#CREE TOUS LES COMPOSANTS DE TYPE 74HC_00 À 74HC_86 AVEC 7 BROCHES OU PINS
class Composant74HC:  
    def __init__(self, nom, coordonnee_TROU,numero_pin=0):
        """
        Initialise un composant 74HC00 avec ses broches.
        :param nom: Nom unique du composant.
        """
        self.nom = f"74HC{nom}" # on ajoute 74HC_00
        self.broches = {
            "1": f"e{coordonnee_TROU + 0}",  # INPUT 1 Porte NAND 1
            "type_1": f"INPUT",
            "numero_pin_1": f"1", # pour dire le pin 1 du 74HC00
            ##"etat": "NOT_CONNECTED", # on a deux etats possibles NOT_CONNECTED ou CONNECTED
            ##"validite_nand_1": "1",
            ##"etat_valide": "1", # valide non_valide
            "2": f"e{coordonnee_TROU + 1}",  # INPUT 2 Porte NAND 1
            "type_2": f"INPUT",
            "numero_pin_2": f"2",
            "3": f"e{coordonnee_TROU + 2}",  # OUTPUT  Porte NAND 1
            "type_3": f"OUTPUT",
            "numero_pin_3": f"3",
            "4": f"e{coordonnee_TROU + 3}",  # OUTPUT  Porte NAND 2
            "type_4": f"OUTPUT",
            "numero_pin_4": f"4",
            "5": f"e{coordonnee_TROU + 4}",  # INPUT 1 Porte NAND 2
            "type_5": f"INPUT",
            "numero_pin_5": f"5",
            "6": f"e{coordonnee_TROU + 5}",  # INPUT 2 Porte NAND 2
            "type_6": f"INPUT",
            "numero_pin_6": f"6",
            "7": f"e{coordonnee_TROU + 6}", #Broche  (Masse) 
            "type_7": f"PIN_GND",
            "numero_pin_7": f"7",
            "8": f"f{coordonnee_TROU + 6}",  # INPUT 1 Porte NAND 3
            "type_8": f"INPUT",
            "numero_pin_8": f"8",
            "9": f"f{coordonnee_TROU + 5}",   # INPUT 1 Porte NAND 3
            "type_9": f"INPUT",
            "numero_pin_9": f"9",
            "10": f"f{coordonnee_TROU + 4}", # OUTPUT  Porte NAND 3 
            "type_10": f"OUTPUT",
            "numero_pin_10": f"10",
            "11": f"f{coordonnee_TROU + 3}", # OUTPUT  Porte NAND 4 
            "type_11": f"OUTPUT", 
            "numero_pin_11": f"11",
            "12": f"f{coordonnee_TROU + 2}", # INPUT 1 Porte NAND 4
            "type_12": f"INPUT",
            "numero_pin_12": f"12",
            "13": f"f{coordonnee_TROU + 1}", # INPUT 1 Porte NAND 4
            "type_13": f"INPUT",
            "numero_pin_13": f"13",
            "14": f"f{coordonnee_TROU + 0}",   # Broche 14 (Alimentation) 
            "type_14": f"PIN_VCC",
            "numero_pin_14": f"14"
        }
    ## def est_valide_porte_nand(n):
    ##     return "Valide" if n % 2 == 0 else "Invalide"

    ## ++++ LE GRAPHE EST LE GESTIONNAIRE DES COMPOSANTS ###
    ##  LE GRAPHE CONNAIT TOUS LES ELEMENTS (COMPOSANTS MAIS PAS LE COMPOSANT) DU BREADBOARD    
    # def connecter(self, broche, cible):
    #     """
    #     Connecte une broche du composant à une autre.
    #     :param broche: La broche source à connecter.
    #     :param cible: Le composant ou la broche cible.
    #     """
    #     if broche in self.broches:
    #         self.broches[broche] = cible
    #     else:
    #         print(f"Erreur : {broche} n'est pas une broche valide du 74HC00.")


    # def __repr__(self):
    #     return f"74HC({self.nom})"
    
class composant_input:  
    def __init__(self, coordonnees_x_y, type, numero_pin=0):
        """
        Initialise un composant composant_input avec ses broches.
        :param nom_numero_unique: Nom unique du composant.
        """
        self.nom = coordonnees_x_y
        self.type = type 
        self.broches = {
            "1": f"{coordonnees_x_y}", # c'est un trou sur la breadboard
            "type": f"{type}",  ## c'est une entree 
            "numero_pin": f"{numero_pin}",
        }

class composant_output:  
    def __init__(self, coordonnees_x_y, type, numero_pin=0): ## initialise a zero par defaut
        """
        Initialise un composant composant_output avec ses broches.
        :param nom_numero_unique: Nom unique du composant.
        """
        self.nom = coordonnees_x_y 
        self.type = type 
        self.broches = {
            "1": f"{coordonnees_x_y}", # c'est un trou sur la breadboard
            "type": f"{type}", ## c'est une sortie
            "numero_pin": f"{numero_pin}",
        }
        

# import networkx as nx

def detect_court_circuits(graph):
    """
    Détecte un court-circuit si un chemin direct entre VCC et GND existe sans résistance.
    """
    # for un_node in graph.nodes:
    #     if un_node.broches["type"]=="VCC":
    #         print(un_node)
    # un composant ayant un pin de numero different de 0 est un input, output, wire de type power
    # 
    vcc_nodes = [un_node for un_node in graph.nodes if un_node.broches["type"]=="VCC"]
    gnd_nodes = [un_node for un_node in graph.nodes if un_node.broches["type"]=="GND"]

    if not vcc_nodes or not gnd_nodes:
        print("⚠️ Erreur : Aucun nœud VCC ou GND trouvé.")
        return

    for vcc in vcc_nodes:
        for gnd in gnd_nodes:
            if nx.has_path(graph, vcc, gnd):  # Vérification d'un chemin entre VCC et GND
                path = nx.shortest_path(graph, vcc, gnd)
                # if all(graph.nodes[n].get("type") in ["WIRE", "VCC", "GND"] for n in path[1:-1]):
                if all(graph.nodes[n].get("type") in ["WIRE",""] for n in path[1:-1]):
                    print(f"⚠️ Court-circuit détecté entre {vcc} et {gnd} via {path}")
                    return
    print("✅ Aucun court-circuit détecté.")

def detect_circuits_ouvert(graph):
    """
    Vérifie si des circuits ouverts existent en s'assurant que chaque VCC a un chemin vers GND.
    """
    vcc_nodes = [node for node in graph.nodes if graph.nodes[node].get("type") == "VCC"]
    gnd_nodes = [node for node in graph.nodes if graph.nodes[node].get("type") == "GND"]

    open_circuits = []

    for vcc in vcc_nodes:
        if not any(nx.has_path(graph, vcc, gnd) for gnd in gnd_nodes):
            open_circuits.append(vcc)

    if open_circuits:
        print(f"⚠️ Circuits ouverts détectés sur : {open_circuits} (aucune connexion à GND)")
    else:
        print("✅ Aucun circuit ouvert détecté.")


# def detect_open_circuits(graph):
#     """
#     Détecte les circuits ouverts dans le graphe en vérifiant s'il existe un chemin
#     entre les nœuds VCC et de masse GND ainsi qu'entre les composants connectés.
#     """
#     open_circuits = []

#     # Vérifier si tous les composants connectés à VCC ont un chemin vers GND
#     for node in graph.nodes:
#         if graph.nodes[node].get("type") == "VCC":
#             if not nx.has_path(graph, node, "GND"):
#                 open_circuits.append(node)

#     if open_circuits:
#         print(f"⚠️ Circuits ouverts détectés sur les nœuds suivants (non connectés à GND) : {open_circuits}")
#     else:
#         print("✅ Aucun circuit ouvert détecté.")

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




# POUR L'INSTANT ON NE GERE PAS L HORLOGE

# class wire_breadboard:  
#     def __init__(self, nom_numero_unique, coordonnee_deux_trous, types):
#         """
#         Initialise un composant wire_breadboard avec ses broches.
#         :param nom_numero_unique: Nom unique du composant.
#         """
#         self.nom = nom_numero_unique 
#         self.broches = {
#             "1": f"{coordonnee_deux_trous[0]}{coordonnee_deux_trous[1]}", 
#             "2": f"{coordonnee_deux_trous[2]}{coordonnee_deux_trous[3]}",
#             "type_broche_1": f"{types[0]}",
#             "type_broche_2": f"{types[1]}"
#         }       

# class vcc_alimentation:  
#     def __init__(self, nom_numero_unique, type, coordonnees_x_y):
#         """
#         Initialise un composant vcc_alimentation avec ses broches.
#         :param nom_numero_unique: Nom unique du composant.
#         """
#         self.nom = nom_numero_unique 
#         self.type = type 
#         self.coordonnees_x_y=coordonnees_x_y
#         self.broches = {
#             "1": f"{coordonnees_x_y["coordonnees_x"]} {coordonnees_x_y["coordonnees_y"]}", # ++
#             "type":f"{type}"
#         }
# Le trou peut etre de type {INPUT, OUTPUT, VCC, GND, CLOCK, WIRE, VIDE}
# Les etats sont de type {CONNECTED, NOT CONNECTED, VALIDE, INVALIDE}
# Les wire sont des edges pas des composants fonctionnels
class trou:  
    def __init__(self, coordonnees_x_y,type, numero_pin=0): ## on donne 0 par defaut au numero de pin
        """
        Initialise un composant vcc_alimentation avec ses broches.
        :param nom_numero_unique: Nom unique du composant.
        """
        self.nom = coordonnees_x_y 
        self.type = type 
        self.coordonnees_x_y=coordonnees_x_y
        #self.etat = "INVALIDE"

        # line 133        
        # return f"{self.broches["1"]}, {self.broches["type"]}"  # Affichage personnalisé 
        #                    ^
        # SyntaxError: f-string: unmatched '['
        self.broches = {
            "1": f"{self.coordonnees_x_y}", #
            "type" : f"{type}",
            "numero_pin": f"{numero_pin}"
        }

        # self.broches = (f"{self.coordonnees_x_y}",f"{type}")
    
    def __hash__(self):
        return hash(self.coordonnees_x_y)
    
    # Definir les operateurs de comparaison
    # Facilite la manipulation des objets : comparaisons

    def __eq__(self, autre_trou):
        """Surcharge de l'opérateur == (égalité)"""
        return self.coordonnees_x_y == autre_trou.coordonnees_x_y
        
        # def __ne__(self, autre_trou):
        #     """Surcharge de l'opérateur != (différent)"""
        #     return self.coordonnees_x_y != autre_trou.coordonnees_x_y

        # def __lt__(self, autre_trou):
        #     """Surcharge de l'opérateur < (inférieur à)"""
        #     return self.coordonnees_x_y < autre_trou.coordonnees_x_y

        # def __gt__(self, autre_trou):
        #     """Surcharge de l'opérateur > (supérieur à)"""
        #     return self.coordonnees_x_y > autre_trou.coordonnees_x_y

        
    def __str__(self):
#        return f"{self.broches["1"]}, {self.broches["type"]}"  # Affichage personnalisé du trou
        return fr"{self.nom}, {self.type}"  # Affichage personnalisé du trou


def adresse_contient_le_chiffre(chiffre_recherche, chaine):
    """
    Vérifie si une chaîne contient exactement 'a7'.
    """
    pattern = fr"{chiffre_recherche}"  # Recherche exacte de "7"
    # pattern = f"r[{chiffre_recherche}-{chiffre_recherche}]"  # Recherche exacte de "7"
    # pattern = fr"7"
    # Utilisation de re.search()
    if re.search(pattern, chaine):
        return True
    return False

##########################################################################
#                FIN DE LA CREATION DE LA CLASSE COMPOSANT               #          #
##########################################################################
# Création du graphe de trous 
G = nx.Graph()

# Le graphe connait que des trous et gere le circuit qu'à partir des trous 
# debut_broches_composant74HC=7

# Creation de la list des trous à connecter aux broches et trous 
# Création des composants 74HC00

composant74HC_1 = Composant74HC("00-1", 7) # le composant possede ses broches en interne
#composant74HC_2 = Composant74HC("00-2", 24)
##on ajoute ces trous au graphe G

# trou_temp_1=trou(composant74HC_1.broches["1"], composant74HC_1.broches["type_1"])
# trou_temp_2=trou(composant74HC_1.broches["2"], composant74HC_1.broches["type_2"])
# trou_temp_3=trou(composant74HC_1.broches["3"], composant74HC_1.broches["type_3"])
# trou_temp_4=trou(composant74HC_1.broches["4"], composant74HC_1.broches["type_4"])
# trou_temp_5=trou(composant74HC_1.broches["5"], composant74HC_1.broches["type_5"])
# trou_temp_6=trou(composant74HC_1.broches["6"], composant74HC_1.broches["type_6"])
# trou_temp_7=trou(composant74HC_1.broches["7"], composant74HC_1.broches["type_7"])
# trou_temp_8=trou(composant74HC_1.broches["8"], composant74HC_1.broches["type_8"])
# trou_temp_9=trou(composant74HC_1.broches["9"], composant74HC_1.broches["type_9"])
# trou_temp_10=trou(composant74HC_1.broches["10"], composant74HC_1.broches["type_10"])
# trou_temp_11=trou(composant74HC_1.broches["11"], composant74HC_1.broches["type_11"])
# trou_temp_12=trou(composant74HC_1.broches["12"], composant74HC_1.broches["type_12"])
# trou_temp_13=trou(composant74HC_1.broches["13"], composant74HC_1.broches["type_13"])
# trou_temp_14=trou(composant74HC_1.broches["14"], composant74HC_1.broches["type_14"])

# G.add_node(trou_temp_1) 
# G.add_node(trou_temp_2) 
# G.add_node(trou_temp_3) 
# G.add_node(trou_temp_4) 
# G.add_node(trou_temp_5) 
# G.add_node(trou_temp_6) 
# G.add_node(trou_temp_7) 
# G.add_node(trou_temp_8) 
# G.add_node(trou_temp_9) 
# G.add_node(trou_temp_10) 
# G.add_node(trou_temp_11) 
# G.add_node(trou_temp_12) 
# G.add_node(trou_temp_13) 
# G.add_node(trou_temp_14) 

for i in range(14):
    temp_i_plus_1=i+1
    # on donne les coordonnees du trou et la fonction de la broche du composant 
    trou_temp=trou(composant74HC_1.broches[f"{temp_i_plus_1}"], composant74HC_1.broches[f"type_{temp_i_plus_1}"], composant74HC_1.broches[f"numero_pin_{temp_i_plus_1}"])
    G.add_node(trou_temp)

# for t in G.nodes:
#     print(t)

composant74HC_2 = Composant74HC("00-2", 24)

for i in range(14):
    temp_i_plus_1=i+1
    trou_temp=trou(composant74HC_2.broches[f"{temp_i_plus_1}"], composant74HC_2.broches[f"type_{temp_i_plus_1}"], composant74HC_1.broches[f"numero_pin_{temp_i_plus_1}"])
    G.add_node(trou_temp)

# for t in G.nodes:
#     print(t)

# composant_input_1 = composant_input("d10", "INPUT")


# Ajout des nœuds
coordonnees_temporaire_trou ="d7"
fonction_temporaire_trou ="INPUT"

trou_temporaire_1=trou(composant_input("d7", "INPUT").broches["1"], composant_input("d7", "INPUT").broches["2"])
trou_temporaire_2=trou(composant_input("d8", "INPUT").broches["1"], composant_input("d8", "INPUT").broches["2"])
trou_temporaire_3=trou(composant_input("d9", "OUTPUT").broches["1"], composant_input("d9", "OUTPUT").broches["2"])


# G.add_node(trou(composant_input("d7", "INPUT").broches["1"], composant_input("d7", "INPUT").broches["2"]))

# G.add_node(trou(composant_input("d8", "INPUT").broches["1"], composant_input("d8", "INPUT").broches["2"]))

# G.add_node(trou(composant_input("d9", "OUTPUT").broches["1"], composant_input("d9", "OUTPUT").broches["2"]))
G.add_node(trou_temporaire_1)
G.add_node(trou_temporaire_2)
G.add_node(trou_temporaire_3)

# Rechercher le trou avec les coordonnes "e7" et de type INPUT
temp_1 = trou("e7","INPUT")
temp_2 = trou("e8","INPUT")
temp_3 = trou("e9","OUTPUT")

for noeud_recherche in G.nodes:
    if noeud_recherche == temp_1:
        G.add_edge(noeud_recherche , trou_temporaire_1)
    if noeud_recherche == temp_2:
        G.add_edge(noeud_recherche , trou_temporaire_2)
    if noeud_recherche == temp_3:
        G.add_edge(noeud_recherche , trou_temporaire_3)


## A tester
# noeud_trouve = next((n for n in G.nodes if n == 50000), None)
##

temp_4 = trou("p3", "VCC")
temp_5 = trou("n3", "GND")
G.add_node(temp_4)
G.add_node(temp_5)
G.add_edge(temp_4, temp_5) 

temp_6 = trou("p4", "VCC")
temp_7 = trou("d4", "WIRE")
G.add_node(temp_6)
G.add_node(temp_7)
G.add_edge(temp_6 , temp_7) 

temp_8 = trou("a4", "WIRE")
G.add_node(temp_8)
G.add_edge(temp_8 , temp_7)

temp_9 = trou("a18", "WIRE")
G.add_node(temp_9)
G.add_edge(temp_8 , temp_9)

temp_10 = trou("c18", "WIRE")
G.add_node(temp_10)
G.add_edge(temp_9 , temp_10)

temp_11 = trou("n18", "GND")
G.add_node(temp_11)
G.add_edge(temp_10 , temp_11)

temp_12 = trou("e13", "GND")
temp_13 = trou("c13", "WIRE")
G.add_node(temp_13)
for noeud_recherche in G.nodes:
    if noeud_recherche == temp_12:   
        G.add_edge(noeud_recherche , temp_13)
        break
    
temp_14 = trou("c16", "WIRE")
G.add_node(temp_14)
G.add_edge(temp_13 , temp_14)

temp_15 = trou("e16", "WIRE")
G.add_node(temp_15)
G.add_edge(temp_14 , temp_15)

temp_16 = trou("n16", "GND")
G.add_node(temp_16)
G.add_edge(temp_15 , temp_16)

temp_17 = trou("c18", "WIRE")
G.add_node(temp_17)
G.add_edge(temp_9 , temp_17)

temp_18 = trou("n18", "GND")
G.add_node(temp_18)
G.add_edge(temp_17 , temp_18)


temp_19 = trou("j7", "WIRE")
G.add_node(temp_19)
temp_20 = trou("p7", "VCC")
G.add_node(temp_20)
G.add_edge(temp_19 , temp_20)


print(len(G.nodes))







################################
# for t in G.nodes:
#     #print(t)
#     print(fr" - {t}")
# #########################################################################
# #      commentaire du code 
# #############################################################################
# #FONCTION GERANT LES CONNECTIONS DIRECTES (SANS FIL) SUR abcdefghij 
# # Une fonction qui verifie toujours si un trou doit etre connecte 
# # un deuxieme trou dans le graphe. Cette fonction est appele 
# # avant chaque ajout de trou dans le graphe.
# # Fonction qui recherche dans les noeuds du graphe le repere  "abcdefghij" pour la ligne 7
# # a7, b7, c7, d7,e7, f7,g7,h7,i7,j7 deja connecte 
# chaine_a_to_j="abcdefghij"
# coordonnees_input="d9"
# # position vaut 4
# position=chaine_a_to_j.find(coordonnees_input[0]) #trouve la lettre "d" a la position 4
# if position == -1: # Position non trouvee
#     print(f"Coordonnees du trou non trouvee: {coordonnees_input}")  # -1 (non trouvé)
#     #on va observer si on est connecte avec un autre trou du graphe
#     #on recherche un sommet (trou) du graphe qui a une connection avec ce trou occupe
#     # pour etablir une connection ou un arc du graphe qui
# elif position < 5: # position  valide de 0-9 : # position est trouvee ou coordonnees valide

#     for i in range(5): # position  valide de 0-9: um trou a un 
#         if i == position: # un composant est pose sur le trou et on cherche un 2e trou de broche deja pose
#             print("On saute la position: {position} et pour la lettre: {chaine_a_to_j[position]}!")
#             continue
#             print(i)
#         else: 
#             print("Parcours des nœuds du graphe:")
#             for noeud_recherche in G.nodes:
#                 print(f"- {noeud_recherche}")
#                 chiffre_recherche=noeud_recherche.broches["1"]
#             #    chiffre_recherche=7
#                 if (adresse_contient_le_chiffre(chiffre_recherche[1], trou_temporaire_1.broches["1"])) and (noeud_recherche.nom != trou_temporaire_1.nom): # l adresse contient 7 
#                     print(f"Le nœud {noeud_recherche} existe dans le graphe.")
#                     print(f"Coordonnees du noeud recherche {chaine_a_to_j[i]}{chiffre_recherche} existe dans le graphe.")
#                     # On cree un arc dans le graphe
#                     # entre le trou_temporaire_01 et noeud_recherche qui contient l adresse en chiffre
#                     # Ajout des connexions logiques

#                     G.add_edges_from([(noeud_recherche , trou_temporaire_1)])
#                     break 
# else: # position > 5: # position  valide de 0-9 : # position est trouvee ou coordonnees valide

#     for i in range(5,10): # position  valide de 0-9: um trou a un 
#         if i == position: # un composant est pose sur le trou et on cherche un 2e trou de broche deja pose
#             print("On saute la position: {position} et pour la lettre: {chaine_a_to_j[position]}!")
#             continue
#             print(i)
#         else: 
#             print("Parcours des nœuds du graphe:")
#             for noeud_recherche in G.nodes:
#                 print(f"- {noeud_recherche}")
#                 chiffre_recherche=noeud_recherche.broches["1"]
#             #    chiffre_recherche=7
#                 if (adresse_contient_le_chiffre(chiffre_recherche[1], trou_temporaire_1.broches["1"])) and (noeud_recherche.nom != trou_temporaire_1.nom): # l adresse contient 7 
#                     print(f"Le nœud {noeud_recherche} existe dans le graphe.")
#                     print(f"Coordonnees du noeud recherche {chaine_a_to_j[i]}{chiffre_recherche} existe dans le graphe.")
#                     # On cree un arc dans le graphe
#                     # entre le trou_temporaire_01 et noeud_recherche qui contient l adresse en chiffre
#                     # Ajout des connexions logiques
#                     G.add_edges_from([(noeud_recherche , trou_temporaire_1)])
#                     break 
###################################################################################
###################################################################################

# Affichage des composants et connexions
# print("Composants et connexions dans le graphe :")
# for node in G.nodes:
#     print(node)

# print("\nConnexions du graphe :")
# for edge in G.edges:
#     print(f"{edge[0]}  →  {edge[1]}")


#G.add_node('VCC', type='power')

print(G)

detect_court_circuits(G) 
detect_circuits_ouvert(G)


# G.add_node('VCC', type='power')
# G.add_node('GND', type='ground')



#60 trous pour connecter les VCC
# G.add_node('T1', type='trou')
# G.add_node('T2', type='trou')

# G.add_node('C2_0', type='wire')
# G.add_node('C2_1', type='wire')

# Ajout des arêtes (connexions)
# G.add_edge('VCC', 'R1')
# G.add_edge('R1', 'LED1')
# G.add_edge('LED1', 'GND')

# G.add_edge('VCC', 'T1')
# G.add_edge('T1', 'T2')
# G.add_edge('T2', 'GND')






# # Ajout de nœuds représentant des broches Arduino
# G.add_node('D2', type='arduino_pin', io='output')
# G.add_node('D3', type='arduino_pin', io='input')

# # Connexion correcte : D2 (sortie) vers LED1
# G.add_edge('D2', 'LED1')

# # Connexion incorrecte : D2 (sortie) vers D3 (entrée)
# G.add_edge('D2', 'D3')

# # Détection des connexions incorrectes
# def detect_io_errors(graph):
#     for u, v in graph.edges:
#         u_attr = graph.nodes[u]
#         v_attr = graph.nodes[v]
#         if u_attr.get('type') == 'arduino_pin' and v_attr.get('type') == 'arduino_pin':
#             if u_attr.get('io') == 'output' and v_attr.get('io') == 'output':
#                 print(f"Erreur : Connexion entre deux sorties {u} et {v}.")
#             elif u_attr.get('io') == 'input' and v_attr.get('io') == 'input':
#                 print(f"Erreur : Connexion entre deux entrées {u} et {v}.")
#             elif u_attr.get('io') == 'output' and v_attr.get('io') == 'input':
#                 print(f"Connexion correcte entre {u} (sortie) et {v} (entrée).")

# detect_io_errors(G)



# Ajout d'une connexion incorrecte provoquant un court-circuit
####G.add_edge('VCC', 'GND')



# G.remove_edge('R1', 'LED1')

# # Détection des circuits ouverts
# def detect_open_circuits(graph):
#     power_nodes = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'power']
#     ground_nodes = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'ground']
#     for component in graph.nodes:
#         if graph.nodes[component].get('type') not in ['power', 'ground']:
#             connected_to_power = any(nx.has_path(graph, component, p_node) for p_node in power_nodes)
#             connected_to_ground = any(nx.has_path(graph, component, g_node) for g_node in ground_nodes)
#             if not (connected_to_power and connected_to_ground):
#                 print(f"Circuit ouvert détecté au niveau du composant {component}.")

# Suppression de la connexion entre R1 et LED1 pour simuler un circuit ouvert

# detect_open_circuits(G)
#G.add_edge('R1', 'LED1')
#detect_open_circuits(G)

# #################################################
# #Détection des courts-circuits
# def detect_short_circuits(graph):
#     # power_nodes = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'power']
#     # ground_nodes = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'ground']
#     # for p_node in power_nodes:
#     #     for g_node in ground_nodes:
#     #         if nx.has_path(graph, p_node, g_node) and {p_node} == "VCC" and {g_node} == "GND":
#     #             print(f"Court-circuit détecté entre {p_node} et {g_node}.")
#     if nx.has_path(graph, "VCC", "GND"):
#         #nx.shortest_path(graph, "VCC", "GND")
#         list_of_path=nx.all_shortest_paths(graph, "VCC", "GND")
#         for  lst_node in list_of_path:
#             l=  lst_node
#             node_type = [graph.nodes[node]["type"] for node in l[1:-1]]
#         print(f"Court-circuit détecté entre VCC et GND.")
# # G.remove_edge('VCC', 'GND')

# detect_short_circuits(G)
#electronique puce, vcc ground, puce vcc, vcc sur sortie, ground sur sortie, vcc sur
#  id puce, 



#3. Analyse du graphe :
#Une fois le circuit représenté sous forme de graphe, vous pouvez utiliser les fonctionnalités 
# de NetworkX pour analyser le circuit. Par exemple, pour vérifier s'il existe un chemin entre 
# la source de tension et la masse 

# Vérification de la connectivité entre la source de tension et la masse
# if nx.has_path(G, 'power', 'ground'):
#     print("Il existe un chemin entre la source de tension et la masse.")
# else:
#     print("Aucun chemin n'existe entre la source de tension et la masse.")

# 

# detect_short_circuits(G)



####################### Elements non connectes #############################

# import networkx as nx

# # Création du graphe du circuit
# G = nx.Graph()

# # Ajout des nœuds représentant les composants
# G.add_node('VCC', type='power')
# G.add_node('GND', type='ground')
# G.add_node('R1', type='resistor')
# G.add_node('LED1', type='led')
# G.add_node('D2', type='arduino_pin', io='output')

# # Ajout des connexions correctes
# G.add_edge('VCC', 'R1')
# G.add_edge('R1', 'LED1')
# G.add_edge('LED1', 'GND')

# # Ajout d'un composant non connecté (erreur)
# G.add_node('R2', type='resistor')  # R2 n'a aucune connexion

# # Fonction de détection des composants non connectés
# def detect_unconnected_components(graph):
#     connected_nodes = set()
    
#     # Identifier les composants atteignables depuis l'alimentation (VCC) ou la masse (GND)
#     for source in ['VCC', 'GND']:
#         if source in graph:
#             reachable = nx.node_connected_component(graph, source)
#             connected_nodes.update(reachable)

#     # Rechercher les composants isolés
#     for node in graph.nodes:
#         if node not in connected_nodes:
#             print(f"⚠️ Composant non connecté détecté : {node}")

# # Exécuter la détection
# detect_unconnected_components(G)
