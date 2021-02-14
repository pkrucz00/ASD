from math import inf

def floyd_warshall(G):
    n = len(G)
    D = G[:]
    for i in range(n):
        D[i][i] = 0
    P = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and G[i][j] < inf:
                P[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]

    return P

def printFloyd(P, s, t):
    if P[s][t] != None:
        result = str(t)
        t = P[s][t]
        while P[s][t] != None:
            result = str(t) + "->" + result
            t = P[s][t]
        result = str(s) + "->" + result
        print(result)

G = [[0, 3, 8, inf, -4],
     [inf, 0, inf, 1, 7],
     [inf, 4, 0, inf, inf],
     [2, inf, -5, 0, inf],
     [inf, inf, inf, 6, 0]]
P = floyd_warshall(G)
printFloyd(P, 4, 1)