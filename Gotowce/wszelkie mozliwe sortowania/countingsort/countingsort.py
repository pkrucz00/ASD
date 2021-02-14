def countingSort(A):
    n = len(A)
    result = [0] * n
    k = max(A)+1
    aux = [0] * k

    for i in range(n):
        aux[A[i]] += 1
    for i in range(1, k):
        aux[i] += aux[i-1]
    for i in range(n-1, -1, -1):
        result[aux[A[i]]-1] = A[i]
        aux[A[i]] -= 1

    for i in range(n):
        A[i] = result[i]

A = [2,3,4,3,5,4,3,2,1,4,3,5]
countingSort(A)
print(A)