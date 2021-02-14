class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskall(G):
    n = len(G)
    edges = []      #stworzenie listy krawedzi
    for u in range(n):
        for v in range(n):
            w = G[u][v]
            if w > 0:
                edges.append((w, u, v))
    edges.sort()    #posortowanie według wag

    sets = [Node(i) for i in range(n)]  #inicjalizacja zbiorow

    MST = []
    for w, u, v in edges:
        if find_set(sets[u]) != find_set(sets[v]):
            MST.append((u,v))
            union(sets[u],sets[v])

    return MST

G = [[0,1,2,5],
     [1,0,3,2],
     [2,3,0,0],
     [5,2,0,0]]
print(kruskall(G))

