def insertionSort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

A = [1, 4, 5, 6, 3, 7, 2, 8]
insertionSort(A)
print(A)