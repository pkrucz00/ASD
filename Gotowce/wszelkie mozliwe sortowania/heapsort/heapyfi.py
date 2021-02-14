def heapify(A, i):
    n = A[0]
    largest = i
    left = 2*i
    right = 2*i+1
    if left <= n and A[left] > A[largest]:
        largest= left
    if right <= n and A[right] > A[largest]:
        largest= right
    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, largest)

def heapsort(A):
    n = A[0]
    for i in range((n//2), 0, -1):
        heapify(A, i)
    for i in range(n, 0, -1):
        A[1], A[i] = A[i], A[1]
        A[0] -= 1
        heapify(A, 1)


A = [1,7,4,3,5,6,2,8,9]
A = [len(A)] + A
print(A)
heapsort(A)
print(A)
