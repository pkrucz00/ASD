from math import inf

class Vertex:
    def __init__(self, ind):
        self.ind=ind
        self.dist=inf
        self.parent=None

def relax(vert, u, v, d):
    if vert[v].dist > vert[u].dist + d:
        vert[v].dist = vert[u].dist + d
        vert[v].parent=u

def bellman_ford(G, s):
    n = len(G)
    vertices = [None]*n
    for i in range(n):
        vertices[i] = Vertex(i)
    vertices[s].dist = 0

    for i in range(n-1):
        for u in range(n):
            for v, d in G[u]:
                relax(vertices, u, v, d)

    for u in range(n):
        for v, d in G[u]:
            if vertices[v].dist > vertices[u].dist + d:
                return False
    return [v.dist for v in vertices]



G = [[(1,3), (6,2)],
     [(0,3), (2,2), (3,1)],
     [(1,2), (4,5)],
     [(1,1), (4,1), (5,7)],
     [(2,5), (3,1), (8,20)],
     [(3,7), (6,1), (7,1), (8,2)],
     [(0,2), (5,1), (7,3)],
     [(5,1), (6,3), (8,8)],
     [(4,20), (5,2), (7,8)] ]
print( bellman_ford( G, 0 ) )