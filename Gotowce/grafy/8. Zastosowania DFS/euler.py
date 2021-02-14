def DFSVisit(G, result, v):
    while not len(G[v])==0:
        u = G[v][0]
        G[v].remove(u)
        G[u].remove(v)
        DFSVisit(G, result, u)

    result.append(v)

def DFS(G):
    result = []
    DFSVisit(G, result, 0)

    return result   #zmienna time nie jest potrzebna do zdobycia odpowiedniego rezultatu, ale co to za DFS bez znakow czasowych

G = [[1,5], [0,2,5,6], [1,6,3,4], [2,4], [2,3,5,6], [0,1,4,6], [1,2,4,5]]
print( DFS(G) )