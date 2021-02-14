def partition(A, p, r):
    i = p
    for j in range(p, r):
        if A[r] > A[j]:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def shallowQuickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if (q - p < r -q):
            shallowQuickSort(A, p, q-1)
            p = q+1
        else:
            shallowQuickSort(A, q+1, r)
            r = q-1


A = [3,5,2,7,6,8,4,1,9,10, 4, 7, 24, 3,456,4,45,69,2,6,2,4,57,2]
shallowQuickSort(A, 0, len(A)-1)
print(A)