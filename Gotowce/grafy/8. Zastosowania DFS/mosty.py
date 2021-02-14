class Vertex:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.color = 0
        self.entered = None
        self.exited = None
        self.reverse_edge = None
        self.low = None

def low(i, vList):
    v = vList[i]
    if v.reverse_edge is not None:
        u = vList[v.reverse_edge]
        while u != v:
            if v.low < u.low:
                v.low = u.low
            v = vList[v.parent]



def DFSVisit(v, time, vList, G):
    time[0] += 1
    v.color = 1
    v.entered = time[0]
    for i in G[v.index]:    #wszystkie wierzcholki
        u = vList[i]
        if u.color == 1:
            v.reverse_edge = u.index
        if  u.color == 0:
            u.parent = v.index
            DFSVisit(u, time, vList, G)
    time[0] += 1
    v.exited = time[0]
    v.color = 2

def Bridges(G):
    time = [0]      #  wyglada to dziwnie, ale do funkcji nalezy przekazac obiekt typu mutable (w tym wypadku liste), aby zachowywal sie jak przekazany przez referencje
    n = len(G)      #  rzad grafu
    vList = [None] * n

    for i in range(n):
        vList[i] = Vertex(i)    #zapisujemy najwazniejsze informacje o danym wierzcholku w liscie

    for v in vList:
        if v.color==0:
            DFSVisit(v, time, vList, G)
        v.low = v.entered

    for i in range(n):
        low(i, vList)

    return [(v.index, v.parent) for v in vList if v.entered == v.low]

G = [[1,3],[0,2],[3,1,4],[0,2],[2,5,6], [4,6], [4,5]]
print( Bridges(G) )