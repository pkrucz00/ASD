def partition(A, p, r):
    i = p
    for j in range(p, r):
        if A[r] > A[j]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[r], A[i] = A[i], A[r]
    return i


def select(A, i, p, r):
    if p == r:
        return A[r]
    q = partition(A, p, r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i < k:
        return select(A, i, p, q-1)
    else:
        return select(A, i-k, q+1, r)

A = [3,6,2,5,4,7,1,8,9]
print(select(A, 7, 0, len(A)-1))