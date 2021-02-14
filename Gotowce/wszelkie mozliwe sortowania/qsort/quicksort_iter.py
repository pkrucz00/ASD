class Stack:
    def __init__(self, size):
        self.A = [None]* size
        self.elem = 0
    def push(self, x):
        self.A[self.elem] = x
        self.elem += 1
    def pop(self):
        self.elem -= 1
        return self.A[self.elem]
    def is_empty(self):
        return self.elem == 0

def partition(A, p, r):
    i = p
    for j in range(p, r):
        if A[r] > A[j]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def iterQuickSort(A):
    n = len(A)
    s = Stack(n)
    s.push(n-1)
    s.push(0)
    while not s.is_empty():
        p = s.pop()
        r = s.pop()
        q = partition(A, p, r)
        if p < q-1:
            s.push(q-1)
            s.push(p)
        if q+1 < r:
            s.push(r)
            s.push(q+1)


A = [3,5,2,7,6,8,4,1,9,10, 4, 7, 24, 3,4,5,6,4,5,2,6,2,4,57,2]
iterQuickSort(A)
print(A)