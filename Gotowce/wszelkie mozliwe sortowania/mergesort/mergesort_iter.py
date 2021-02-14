def merge(A, p, q, r):
    n1 = q-p
    n2 = r-q
    left = A[p:q]
    right = A[q:r]
    i = 0
    j = 0

    while i < n1 and j < n2:
        if left[i] < right[j]:
            A[p+i+j] = left[i]
            i += 1
        else:
            A[p+i+j] = right[j]
            j += 1

    while i < n1:
        A[p+i+j] = left[i]
        i += 1
    while j < n2:
        A[p+i+j] = right[j]
        j += 1

def mergeSortIter(A):
    n = len(A)
    if n <= 1:  return A            #warunki brzegowe
    if n == 2:
        merge(A, 0, 1, 2)
        return A

    p, q, r = 0, 1, 2               #p wskazuje na pierwszy indeks przedzialu do posortowania, q na drugi, a r na trzeci
    while True:                 #prosze, nie bij, wiem, ze brzydkie
        while q < n and A[q-1] <= A[q]:
            q += 1
        if q == n:
            if p == 0:
                return A        #warunek wyjscia - jesli q przeszlo przez cala tablice, to znaczy, ze jest posortowana
            p, q, r = 0, 1, 2   #w przeciwnym wypadku (p != 0) na koniec zostaje samotny przedzial, wiec trzeba iterowac od poczatku
            continue

        r = q+1
        while r < n and A[r-1] <= A[r]:
            r += 1

        merge(A, p, q, r)

        if r == n-1 or r == n:      #jesli na koncu zostal przedzial jednoelementowy lub nie zostalo nic - iterujemy od poczatku
            p, q, r = 0, 1, 2
        else:
            p, q, r = r, r+1, r+2



A = [5,6,8,0,7,4,8,1,0,5,8,3,7,6]
mergeSortIter(A)
print(A)