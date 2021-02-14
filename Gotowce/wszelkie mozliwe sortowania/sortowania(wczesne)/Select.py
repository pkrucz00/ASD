def Select(A, k):
    first = 0
    last = len(A)
    i = partition( A, first, last)
    if k == i: return A[i]
    elif k < i return Select(A[:i],k)
    else:   return Select(A[i+1:], k-i)

