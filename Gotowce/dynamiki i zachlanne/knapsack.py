def Knapsack(W, P, MaxW):
    n = len(W)
    F = [None]*n
    for i in range(n):
        F[i] = [0]*(MaxW+1)
    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]
    for i in range(1,n):
        for w in range(1,MaxW+1):
            F[i][w] = F[i][w-1]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])
    return F[n-1][MaxW]

