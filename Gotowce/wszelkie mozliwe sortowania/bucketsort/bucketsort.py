def bucketsort(A):
    n = len(A)
    if n <= 1:
        return A
    high = max(A)
    low = min(A)
    interval = high - low   #zakladamy rownomierny rozklad wartosci na danym przedziale
    buckets = [ [] for _ in range(n+1)]

    for elem in A:
        key = int(n*((elem-low)/interval))
        buckets[key].append(elem)
    for bucket in buckets:
        bucketsort(bucket)
    A = []
    for i in range(n+1):
        A += buckets[i]
    return A

A = [7.84, 6.42, 2.42, 4.52, 3.26]
print(bucketsort(A))


