class Vertex:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.visited = False
        self.entered = None
        self.exited = None



def DFS(G):
    def DFSVisit(v, time, vList, G):
        time[0] += 1
        v.visited = True
        v.entered = time[0]
        for i in G[v.index]:  # wszystkie wierzcholki
            u = vList[i]  # przypisanie obiektu typu Vertex
            if not u.visited:
                u.parent = v.index
                DFSVisit(u, time, vList, G)
        time[0] += 1
        v.exited = time[0]

    time = [0]      #  wyglada to dziwnie, ale do funkcji nalezy przekazac obiekt typu mutable (w tym wypadku liste), aby zachowywal sie jak przekazany przez referencje
    n = len(G)      #  rzad grafu
    vList = [None] * n

    for i in range(n):
        vList[i] = Vertex(i)    #zapisujemy najwazniejsze informacje o danym wierzcholku w liscie

    for v in vList:
        if not v.visited:
            DFSVisit(v, time, vList, G)

    result = [vList[i].parent for i in range(n)]
    return result   #zmienna time nie jest potrzebna do zdobycia odpowiedniego rezultatu, ale co to za DFS bez znakow czasowych

G = [[1,2],[0,2,3],[3,1,0],[1,2]] 
print( DFS(G) )