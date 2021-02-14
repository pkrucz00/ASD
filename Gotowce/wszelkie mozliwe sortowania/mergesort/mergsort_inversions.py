def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = A[p:q+1]
    right = A[q+1:r+1]
    i = 0
    j = 0
    counter = 0

    while i < n1 and j < n2:
        if left[i] < right[j]:
            A[p+i+j] = left[i]
            i += 1
        else:
            A[p+i+j] = right[j]
            j += 1
            counter += n1 - i

    while i < n1:
        A[p+i+j] = left[i]
        i += 1
    while j < n2:
        A[p+i+j] = right[j]
        j += 1
    return counter

def MergeSort(A, p, r):
    if p < r:
        q = (r + p)//2
        c = MergeSort(A, p, q)
        c += MergeSort(A, q+1, r)
        c += merge(A,p,q,r)
        return c
    else:
        return 0

A = [1,2,3,6,5,4]
print(MergeSort(A, 0, len(A)-1))
print(A)