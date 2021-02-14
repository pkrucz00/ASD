from queue import *
from math import *


class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None
        self.d = inf


def dijkstra(G, w, s):
    n = len(G)
    vrtx = [None] * n
    for i in range(n):
        vrtx[i] = Vertex(i)
    s = vrtx[s]
    s.d = 0
    Q = PriorityQueue()
    Q.put((s.d, s.idx))
    while not Q.empty():
        dis, u = Q.get()
        for v in G[u]:
            v = vrtx[v]
            if v.d > dis + w[u][v.idx]:
                v.d = dis + w[u][v.idx]
                v.parent = u
                Q.put((v.d, v.idx))
    return vrtx


def print_d(vrtx):
    for u in vrtx:
        print(u.idx, u.d)


G = [
    [1, 6],
    [0, 2, 3],
    [1, 4],
    [1, 5, 4],
    [2, 3, 8],
    [3, 6, 7, 8],
    [0, 5, 7],
    [5, 6, 8],
    [5, 7, 4]
]

w = [
    [0, 3, 0, 0, 0, 0, 2, 0, 0],
    [3, 0, 2, 1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 5, 7, 0, 0, 0],
    [0, 0, 1, 5, 0, 0, 0, 0, 20],
    [0, 0, 0, 7, 0, 0, 1, 1, 2],
    [2, 0, 0, 0, 0, 1, 0, 3, 0],
    [0, 0, 0, 0, 0, 1, 3, 0, 8],
    [0, 0, 0, 0, 20, 2, 0, 8, 0]
]

vrtx = dijkstra(G, w, 0)
print_d(vrtx)