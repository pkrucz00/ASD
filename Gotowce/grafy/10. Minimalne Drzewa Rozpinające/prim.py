
from queue import PriorityQueue
from math import inf

def Prim(G):
    n = len(G)
    queue = PriorityQueue()
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]

    distance[0] = 0

    queue.put((0,distance[0]))

    while not queue.empty():
        u, d = queue.get()
        for v in range(n):
            if G[u][v] > 0 and distance[v] > G[u][v]:
                distance[v] = G[u][v]
                parent[v] = u
                queue.put((v, distance[v]))

    return [(parent[i], i) for i in range(n) if parent[i] is not None]

G = [[0,1,2,5],
     [1,0,3,2],
     [2,3,0,0],
     [5,2,0,0]]
print(Prim(G))

