class Vertex:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.visited = False
        self.entered = None
        self.exited = None

def DFSVisit(v, time, vList, G):
    time[0] += 1
    v.visited = True
    v.entered = time[0]
    for i in G[v.index]:    #wszystkie wierzcholki
        u = vList[i]        #przypisanie obiektu typu Vertex
        if not u.visited:
            u.parent = v.index
            DFSVisit(u, time, vList, G)
    time[0] += 1
    v.exited = time[0]

def DFSrev(v, vList, G, result):
    v.visited = True
    for i in G[v.index]:
        u = vList[i]
        if not u.visited:
            DFSrev(u, vList, G, result)
    result.append(v.index)


def reverse_graph(G):
    result = [ [] for _ in range(len(G))]
    for v in range(len(G)):
        for u in G[v]:
            result[u].append(v)
    return result



def Sil_sp_skl(G):
    time = [0]
    n = len(G)      #  rzad grafu
    vList = [None] * n

    for i in range(n):
        vList[i] = Vertex(i)    #zapisujemy najwazniejsze informacje o danym wierzcholku w liscie

    for v in vList:
        if not v.visited:
            DFSVisit(v, time, vList, G)

    G_rev = reverse_graph(G)
    time[0] = 0
    times = [(vList[i].exited,i) for i in range(n)]
    times.sort(reverse=True)
    SCC = []

    for v in vList:
        v.visited = False

    for exit_time, v in times:
        if not vList[v].visited:
            SCC.append([])
            DFSrev(vList[v],vList, G_rev, SCC[len(SCC)-1])

    return SCC


G = [ [2,4],
      [0,9],
      [1],
      [4,6],
      [5],
      [3],
      [5],
      [3,9],
      [7],
      [10],
      [6,8]]
print( Sil_sp_skl(G) )