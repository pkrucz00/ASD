def binarySearch(A, x, p, r):
    if r < p:
        return None
    q = (p+r)//2
    if A[q] == x:
        return q
    elif x > A[q]:
        return binarySearch(A, x, q+1, r)
    else:
        return binarySearch(A, x, p, q-1)

A = [1,4,5,6,8,9,10,23,24,27,134,342,657]
print(binarySearch(A, 23, 0, len(A)-1))