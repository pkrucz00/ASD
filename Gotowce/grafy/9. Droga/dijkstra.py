from queue import PriorityQueue
from math import inf

def dijkstra( G, s ):
    n = len(G)

    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = PriorityQueue()

    distance[s] = 0
    queue.put( (s,distance[s]) )
    while not queue.empty():
        u, d = queue.get()
        for v, weight in G[u]:
            if distance[v] > d + weight:
                distance[v] = d + weight
                parent[v] = u
                queue.put((v,distance[v]))
    return distance


G = [[(1,3), (6,2)],
     [(0,3), (2,2), (3,1)],
     [(1,2), (4,5)],
     [(1,1), (4,1), (5,7)],
     [(2,5), (3,1), (8,20)],
     [(3,7), (6,1), (7,1), (8,2)],
     [(0,2), (5,1), (7,3)],
     [(5,1), (6,3), (8,8)],
     [(4,20), (5,2), (7,8)] ]
print( dijkstra( G, 0 ) )  # wypisze [None,0,1,2]