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

def radixsort(A):
    y = 1
    x = 10**y
    n = len(A)
    k = max(A)
    while x < k*10:
        result = [0] * n
        aux = [0] * 10

        for i in range(n):
            key = (A[i]%x)//(x//10)
            aux[key] += 1
        for i in range(1, 10):
            aux[i] += aux[i - 1]
        for i in range(n - 1, -1, -1):
            key = (A[i] % x) // (x // 10)
            result[aux[key]-1] = A[i]
            aux[key] -= 1

        for i in range(n):
            A[i] = result[i]
        y += 1
        x = 10**y
    return A

A = [109,209,384,758,748,367]
print(radixsort(A))