def bubbleSort(A):
    n = len(A)
    for i in range(n, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


A = [4, 5, 6, 2, 5, 7, 8, 3, 2, 6, 1]
bubbleSort(A)
print(A)
