import networkx as nx

class Noeud(): 
    def __init__(self, t = 7):
        self.type_ = t

    

n=Noeud(1) 
n2=Noeud(2)
n3=Noeud(3)
n4=Noeud(4)
n5=Noeud(5)
x=Noeud()
# Création d'un graphe
G = nx.Graph()
G.add_edges_from([
    (n, n2), (n2, n4),
    (x, n3), (n3, n5)  # n3 est isolé de n
])

# Recherche de chemins entre n et [n2, n3]
chemins = list(nx.all_simple_paths(G, source=n, target=[n2,n5, x, n4, n3,]))

print("Chemins trouvés :", chemins)
