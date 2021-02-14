def iterQuickSort(arr):
    n = len(arr)
    S = Stack()
    S.push(n-1)
    S.push(0)

    while not S.is_empty():
        p = S.pop()
        r = S.pop()
        q = partition(arr, p, r)

        if q-1 > p:
            S.push(q-1)
            S.push(p)
        if q+1 < r:
            S.push(r)
            S.push(q+1)
    
