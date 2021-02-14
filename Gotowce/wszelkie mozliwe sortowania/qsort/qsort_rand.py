import random

def partition(A, p, r):
    i = p
    for j in range(p, r):
        if A[r] > A[j]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[r], A[i] = A[i], A[r]
    return i


def randpartition(A, p, r):
    i_rand = random.randint(p, r)
    A[i_rand], A[r] = A[r], A[i_rand]
    return partition(A, p, r)


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


A = [3,5,2,7,6,8,4,1,9,10, 4, 7, 24, 3,4,5,6,4,5,2,6,2,4,57,2]
quickSort(A, 0, len(A)-1)
print(A)